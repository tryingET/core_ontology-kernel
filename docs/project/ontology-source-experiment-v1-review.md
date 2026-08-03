---
summary: "Independent rereview disposition for ontology source experiment protocol v1."
read_when:
  - "Considering execution or reuse of ontology source experiment protocol v1."
type: review
status: final
---

# Ontology source experiment protocol v1 — review disposition

## Reviewed protocol

- Bundle: `ontology-source-experiment-v1/`
- Reviewed protocol digest: `704e0ad9d046cb605942b2137461c1d851f16c684a966f61725625a6cf496728`
- Verdict: **REVISE**
- Execution readiness: **NOT READY**

## Closed blockers

- 40 byte-exact accepted packets and golden-oracle consistency.
- V1 stable relation IDs, V4 guidance schema, and V3 SHACL blank-node boundary.
- Executable complexity calculations.
- Frozen actor/reviewer materials except command allowlist consistency.
- Exact retained-evidence and operator-status byte semantics.

## Remaining blocker

`actor-materials/tool-allowlist.v1.json` does not permit two commands required by the frozen workflow:

- warm-up `./validate-toy`;
- V4 atomic authoring `./experiment author-v4 --root <observation-root> < term-payload.json`.

Runtime waiver, warm-up bypass, or scoring the structurally forbidden V4 command would create post-hoc selection bias. Protocol v2 must add only exact safe argv/redirection forms, receive a new digest, and pass fresh rereview before execution.
