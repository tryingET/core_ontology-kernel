'use strict';

const assert = require('assert/strict');
const crypto = require('crypto');
const fs = require('fs/promises');
const path = require('path');

const editorRoot = process.env.EDITOR_ROOT;
if (!editorRoot) {
  throw new Error('EDITOR_ROOT is required');
}

const {
  Bounds,
  DiagramMetadata,
  DiagramNode,
  OntologyDiagramDocument,
  OntologyFileReference,
  parseOntologyDiagramYaml,
  stringifyOntologyDiagramYaml,
} = require(path.join(editorRoot, 'out/documents/odiagram'));
const { CreateEdgeUseCase } = require(path.join(editorRoot, 'out/diagram-editor/use-cases'));
const { loadReferencedOntologies } = require(path.join(editorRoot, 'out/ui/model-tree/ontology-model'));

const sha256 = (value) => crypto.createHash('sha256').update(value).digest('hex');

async function main() {
  const root = path.resolve(process.argv[2]);
  await fs.mkdir(root, { recursive: true });
  const ontologyPath = path.join(root, 'ontology.ttl');
  const diagramPath = path.join(root, 'probe.odiagram');
  const initialOntology = `@prefix ex: <https://example.com/core#> .\n@prefix owl: <http://www.w3.org/2002/07/owl#> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\nex:Actor a owl:Class ; rdfs:label "Actor" .\nex:Agent a owl:Class ; rdfs:label "Agent" ; rdfs:subClassOf ex:Actor .\n`;
  await fs.writeFile(ontologyPath, initialOntology, 'utf8');

  const baseDiagram = new OntologyDiagramDocument(
    DiagramMetadata.createEmpty('Guarded lens probe'),
    [new OntologyFileReference('ontology.ttl')],
    new Map([
      ['ex', 'https://example.com/core#'],
      ['rdfs', 'http://www.w3.org/2000/01/rdf-schema#'],
    ]),
    [],
    [],
  );
  const diagramYaml = stringifyOntologyDiagramYaml(baseDiagram);
  await fs.writeFile(diagramPath, diagramYaml, 'utf8');

  const sourceBefore = await fs.readFile(ontologyPath);
  const sourceDigestBefore = sha256(sourceBefore);
  const [loaded] = await loadReferencedOntologies(diagramPath, baseDiagram);
  assert.equal(loaded.error, undefined);
  const classesBefore = loaded.items.filter((item) => item.type === 'class');
  const relationship = loaded.items.find((item) => item.type === 'subclassRelationship');
  assert.equal(classesBefore.length, 2);
  assert.ok(relationship, 'expected subclass relationship');

  const noOpRoundTrip = stringifyOntologyDiagramYaml(parseOntologyDiagramYaml(diagramYaml));
  assert.equal(noOpRoundTrip, diagramYaml);
  assert.equal(sha256(await fs.readFile(ontologyPath)), sourceDigestBefore);

  const materialized = new CreateEdgeUseCase().execute(baseDiagram, {
    ontologyItemType: relationship.type,
    ontologyItemReference: relationship.reference,
    displayLabel: relationship.displayLabel,
    ontologyItemMetadata: relationship.metadata,
  }, { x: 240, y: 80 });
  assert.ok(materialized.diagram, 'expected diagram edge materialization');
  assert.equal(materialized.diagram.edges.length, 1);
  const materializedYaml = stringifyOntologyDiagramYaml(materialized.diagram);
  assert.equal(sha256(await fs.readFile(ontologyPath)), sourceDigestBefore);

  const unresolvedDiagram = new OntologyDiagramDocument(
    baseDiagram.metadata,
    baseDiagram.ontologies,
    baseDiagram.namespaces,
    [new DiagramNode('node_missing', 'ex:Missing', new Bounds(0, 0, 96, 44))],
    [],
  );
  const unresolvedYaml = stringifyOntologyDiagramYaml(unresolvedDiagram);
  const unresolvedRoundTrip = parseOntologyDiagramYaml(unresolvedYaml);
  assert.equal(unresolvedRoundTrip.nodes[0].ontologyRef.value, 'ex:Missing');

  const changedOntology = `${initialOntology}ex:Policy a owl:Class ; rdfs:label "Policy" .\n`;
  await fs.writeFile(ontologyPath, changedOntology, 'utf8');
  const [reloaded] = await loadReferencedOntologies(diagramPath, baseDiagram);
  assert.equal(reloaded.error, undefined);
  const classesAfter = reloaded.items.filter((item) => item.type === 'class');
  assert.equal(classesAfter.length, 3);
  assert.equal(await fs.readFile(diagramPath, 'utf8'), diagramYaml);
  assert.ok(!diagramYaml.includes('base_semantic_digest'));
  assert.ok(!diagramYaml.includes('semantic_contract_id'));
  assert.ok(!diagramYaml.includes('projection_profile_id'));

  const receipt = {
    schema: 'ontology-editor-guarded-lens-probe.v0',
    upstream: {
      repository: 'https://github.com/modeldriven-hu/ontology-diagram-editor.git',
      commit: '039b8d9cbe4be1552c0efd29e3ffd5afa2904a6d',
      version: '1.6.0',
    },
    fixture: {
      initial_source_sha256: sourceDigestBefore,
      changed_source_sha256: sha256(Buffer.from(changedOntology)),
      initial_diagram_sha256: sha256(Buffer.from(diagramYaml)),
      materialized_diagram_sha256: sha256(Buffer.from(materializedYaml)),
      class_count_before: classesBefore.length,
      class_count_after: classesAfter.length,
    },
    cases: [
      {
        id: 'C1_NO_OP',
        expected: 'No semantic delta and stable diagram persistence.',
        observed: 'The .odiagram parse/stringify round trip was byte-stable and ontology bytes were unchanged.',
        result: 'pass_for_read_only_projection',
      },
      {
        id: 'C2_SUPPORTED_SEMANTIC_EDIT',
        expected: 'A supported editor action yields a semantic proposal delta.',
        observed: 'Creating the existing subclass edge changed only .odiagram presentation state; ontology bytes and facts were unchanged.',
        result: 'fail_capability_absent',
      },
      {
        id: 'C3_UNSUPPORTED_REFERENCE',
        expected: 'An unsupported or unresolved ontology reference fails closed.',
        observed: 'The .odiagram schema accepted and round-tripped ex:Missing without checking it against the loaded ontology.',
        result: 'fail_without_external_adapter',
      },
      {
        id: 'C4_STALE_BASE',
        expected: 'A changed semantic base is rejected against a bound receipt.',
        observed: 'The ontology reloaded from two to three classes while .odiagram stayed unchanged and carried no semantic-contract, profile, or base-digest binding.',
        result: 'fail_capability_absent',
      },
    ],
    disposition: {
      semantic_proposal_lens: 'fail',
      read_only_visual_projection: 'feasible_with_external_loss_and_freshness_receipts',
      editor_adoption: 'not_authorized',
      source_format_selection: 'not_addressed',
    },
  };

  await fs.writeFile(path.join(root, 'probe-receipt.json'), `${JSON.stringify(receipt, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(receipt, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
