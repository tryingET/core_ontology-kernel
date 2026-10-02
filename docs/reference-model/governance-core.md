---
summary: "Textual reference model for the governance core (AK 5986): the UFO categories, each governance-core concept's category, the parties its records must name and one diagnostic question, and the concepts still open."
read_when:
  - "Before adding, splitting or categorising a governance-core concept"
  - "Before designing a record field (AK decision records, FCOS item contracts) for a governance word"
type: "reference"
---

# Governance core: reference model

This is the reference layer of Guizzardi's architecture: it is written for people and used to agree on meaning. The concept files under `ontology/src/reference/` are the operational layer that tools and agents read. The Holding Owner decided that each governance-core word also states what kind of thing it names (D22) and that the categories come from UFO, Guizzardi's Unified Foundational Ontology (D23, 2026-09-26).

## Rules
1. One meaning and one category per identifier. A concept that names two categories (an act and its outcome, say) is split under CORE-INV-002 (AK 5987).
2. A concept points to its category with an `instance_of` edge, never `is_a`: UFO counts types as instances of meta-types (UFO2022, axioms a1–a4).
3. Only the governance core carries categories: the authority, governance, commitment and check words. MITO segment and level are a separate coordinate, where a thing acts and who owns it, and carry no category.
4. The category tells a record designer what the record must name. A relator names at least two parties; an event record is append-only; phases partition their kind; a role names the relation that makes it true.
5. A category is assigned here, in the reference step, under the Holding Owner's authorization; never by the agent that consumes it.

## The categories

| Identifier | Label | What it is | Test question | Source |
|---|---|---|---|---|
| `core.UfoCategory.Kind` | UFO kind | The UFO category of rigid types that give their instances identity and persistence; an instance cannot stop being one. | Could an instance stop being one and still exist? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 173. |
| `core.UfoCategory.Role` | UFO role | The UFO category of anti-rigid types that apply to an instance only through a relation, which belongs to the role's definition. | Which relation makes the instance play it? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), pp. 173–174. |
| `core.UfoCategory.Phase` | UFO phase | The UFO category of anti-rigid types that apply to an instance through an intrinsic change it can go through; the phases of a kind partition it. | Does the instance enter it by changing itself, with no other party involved? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 173. |
| `core.UfoCategory.Relator` | UFO relator | The UFO category of relational moments that depend on at least two individuals and make a material relation true. | Which two or more parties does it connect? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 172. |
| `core.UfoCategory.Mode` | UFO mode | The UFO category of moments that inhere in one bearer and cannot be measured on a value scale, including dispositions and modes that also depend on others. | Whose is it, and can it be measured on a scale? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 172. |
| `core.UfoCategory.Quality` | UFO quality | The UFO category of moments whose values lie in a quality structure, so that a target is a region of that structure. | On which scale is it measured, and what value counts as met? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 172. |
| `core.UfoCategory.Event` | UFO event | The UFO category of occurrences that unfold in time and cannot change once they have happened; an event takes reality from a pre-state situation to a post-state situation. | Can it change after it happened? | Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), pp. 171, 174; Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §3. |
| `core.UfoCategory.Situation` | UFO situation | The UFO category of states of affairs: portions of reality, made of other entities, that can be comprehended as a whole. | Does it hold or not hold at a given time? | Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §2. |
| `core.UfoCategory.NormativeDescription` | UFO normative description | The UFO-C category of social objects that define rules recognised by at least one social agent, such as regulations, directives and plan descriptions. | Which rules does it define, and who recognises them? | Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §4. |
| `core.UfoCategory.Commitment` | UFO commitment | The UFO-C category of social moments by which one agent is bound towards another to bring about a propositional content; each is paired with a claim. | Who is bound, towards whom, to bring about what? | Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §4; Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 172. |
| `core.UfoCategory.Claim` | UFO claim | The UFO-C category of social moments held by the party a commitment is owed to, paired with that commitment and its propositional content. | Towards whom is a commitment owed? | Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §4. |
| `core.UfoCategory.Proposition` | UFO proposition | The UFO category of propositional contents: abstract representations of the situations that beliefs, desires and intentions refer to; the content of an intention is a goal. | Can a situation satisfy it? | Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §4 and Fig. 3. |
| `core.UfoCategory.HighOrderType` | high-order type | The category, from the multi-level theory MLT that UFO incorporates, of domain types whose instances are themselves domain types; such a type categorises a base type when each of its instances is a proper specialisation of that base type. | Are its instances domain types rather than individuals? | Carvalho, Almeida, Fonseca, Guizzardi (2017), Multi-level ontology-based conceptual modeling, DKE 109, pp. 3–24; Fonseca et al. (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607, pp. 18–34. |

Commitments and claims are externally dependent modes in UFO-A (UFO2022, p. 172); UFO-C names them as social moments that always come in pairs (GFG2008, §4). Permissions, powers and duties (UFO-L, Griffo et al. 2018) are not separate categories here: an authority is a mode (a power), an authorization is the event that uses it and founds a permission, a refusal founds none, and a revocation ends a permission or a delegated authority. Following the Core Ontology on Decision Making (R. Guizzardi, Carneiro, Porello, G. Guizzardi 2020), a decision is an intention (a mode) that a deliberation (an event) creates and a decision-resulting action manifests; authorizations, refusals and revocations are among such actions (AK 6364). Domain types whose instances are domain types belong to the high-order-type category (MLT): `core.DecisionClass` is one: it partitions `core.Proposal`, and its instances, the three class roles, specialise `core.Proposal` and keep their own category (UFO role). The kernel adds high-order type as a sibling category; in OntoUML with high-order types, a high-order type instead specialises the UFO category of its instances (Fonseca et al. 2022, §4.4). UFO also separates roles played by instances of one kind from role mixins played by instances of several kinds; this layer carries only the role category, so a role played by people and agents alike (social role), or by records of different kinds (evidence), is recorded as a UFO role and noted as a role mixin.

## Governance-core concepts

| Concept | Category | Its records must name | Diagnostic question |
|---|---|---|---|
| `core.CarriedObligation` | UFO commitment | who owes it, to whom, the proceed decision, owner and date | Who can dismiss it? Only the party it is owed to. |
| `core.TaskClaim` | UFO commitment | the agent (its session), the requester, the task, the lease; paired with the requester's claim | Who can end it? The agent by releasing it, or the requester by dismissing it; a lease that runs out is a broken commitment. |
| `core.AgreementReview` | UFO event | the agreement, its evaluation criteria, the review date | Does it end in keep, evolve or drop? Yes. |
| `core.AuditEvent` | UFO event | who, what, when, why | Can it change after it happened? No. |
| `core.Authorization` | UFO event | grantor (holding the authority), grantee, scope, basis; it founds a permission | Can an authorization change after it was given? No: a revocation is a new event. |
| `core.ConformanceAudit` | UFO event | the product, its requirements and documentation | Is a product checked against its requirements? Yes. |
| `core.ConsentRound` | UFO event | the proposal, the holders asked, each possible objection with its test result, each objection with its disposition, the end date | Who was asked, and what happened to each possible objection? |
| `core.DecisionGate` | UFO event | the named decider, the criteria set in advance, the work at stake | Does it create or change a permission or commitment? If not, it is a check, not a decision gate. |
| `core.Deliberation` | UFO event | the decider, the motivating intention, the alternatives, the criteria, the decision created | Did it create a decision? It must. |
| `core.Handover` | UFO event | the product, who hands it over, the receiver | Does the receiver get what they need to use it? It must. |
| `core.LeitungReview` | UFO event | the process or system reviewed, the effectiveness question | Does it return a Rückmeldung to Führung? Yes. |
| `core.Operations` | UFO event | the domain whose work it is | Is it doing the work rather than governing it? Yes. |
| `core.ProcessAudit` | UFO event | the process and its process standard | Is a process checked against its standard? Yes. |
| `core.ReadinessReview` | UFO event | decider, criteria set in advance, the item | Does it end in a decision? Yes. |
| `core.Refusal` | UFO event | the refuser, the party refused, what was asked for, the basis | Does it found a permission? No: the proposal returns to its driver. |
| `core.ReplayCheck` | UFO event | the recorded operation and its recorded result | Does a pass show the result is right? No, only that it reproduces. |
| `core.Revocation` | UFO event | the authorizations or delegation it ends, the revoker, the basis | Does it change or delete what it ends? No: those acts stay on record. |
| `core.RoleReview` | UFO event | the role, its holder, the reviewers | Is it about how a role is performed, not about a product? Yes. |
| `core.SchemaCheck` | UFO event | the record or file, the schema | Does a pass say anything beyond the schema? No. |
| `core.Validation` | UFO event | the receiver who judges, the effectiveness metric, the product | Who judged it? It must be the receiver, never the producer. |
| `core.VerificationEvent` | UFO event | the product, the requirement or DoD row, the criteria, the evidence used, the verifier | Can it change after it happened? No: a new check is a new event. |
| `core.WorkProductInspection` | UFO event | the work product and inspectors other than its author | Is the author among the inspectors? No. |
| `core.DecisionClass` | high-order type | its base type `core.Proposal`, its instances (class-A, class-B and class-C change), the rules that assign them | Are its instances types? Yes: the three class roles, each a proper specialisation of `core.Proposal`. |
| `core.DecisionRecord` | UFO kind | the decision and its consent, authorization and dissent records | Is it a record rather than the decision itself? Yes. |
| `core.Dissent` | UFO kind | the objection it keeps and the decision that went ahead over it | Does dissent exist without a decision that went ahead? No. |
| `core.Proposal` | UFO kind | proposer, change, rationale, scope, acceptance criteria | Is it a document that can be reviewed? Yes. |
| `core.Receipt` | UFO kind | the action or artefact, actor, time, content digest | Can it be checked against its digest? Yes. |
| `core.RetainedArtefact` | UFO kind | the content digest, the source, the capture time | Can its bytes be re-verified against its digest? |
| `core.ActorCapability` | UFO mode | the actor or system, what it can do | Could it do this even where it is not permitted to? |
| `core.Authority` | UFO mode | its holder, its scope, and the norm or delegation that created it | Who holds it, for what? |
| `core.Concern` | UFO mode | who holds it, the proposal, agreement or activity, the assumption | Could it block consent? Never. |
| `core.Decision` | UFO mode | the decider, the goal it commits to, the deliberation that created it, the alternatives and criteria weighed | Is it the act of deciding? No: that is the deliberation; the act that carries it out is a decision-resulting action. |
| `core.Objection` | UFO mode | who holds it, the proposal it objects to, its reasons | Has it ended integrated, withdrawn or standing, and did a decision go ahead over it? |
| `core.Permission` | UFO mode | the holder, what it allows, the scope, the authorization or rule that grants it | Who granted it, and within which scope? |
| `core.PossibleObjection` | UFO mode | who raised it, the proposal, agreement or activity, the argument, the test and its result | Has it been tested, and did it qualify? |
| `core.StakeholderExpectation` | UFO mode | the stakeholder who holds it | Who expects this? |
| `core.Directive` | UFO normative description | whom it binds and its owner; tailoring only by relief | May someone depart from it without relief? No. |
| `core.Guidance` | UFO normative description | its owner; it binds no one | May someone depart from it without relief? Yes. |
| `core.Policy` | UFO normative description | whom it binds and its owner | Which rules does it define? |
| `core.Requirement` | UFO normative description | owner, verification method, waiver authority, parent or self-derived flag | Can it be verified? It must be. |
| `core.OperationsMode` | UFO phase | the live system | Is the system live while it changes? Yes. |
| `core.Claim` | UFO proposition | who asserts it, and its scope | Is it an assertion rather than a commitment? Yes. |
| `core.Goal` | UFO proposition | the agent whose intention it is, and the driver it responds to | Whose goal is it? There must be an answer. |
| `core.ArtefactStatus` | UFO quality | the artefact, its value on the scale approach, preliminary, baseline, update | Which of the four values does the artefact hold now? |
| `core.Metric` | UFO quality | what it measures, calculation rule, unit, target | Which value would count as met? |
| `core.TechnologyReadiness` | UFO quality | the technology, the TRL scale, the environment it was shown in | Which level, shown in which environment? |
| `core.ClassAChange` | UFO role | the proposal, the rule that classifies it, who applied it | Which class rule makes this proposal hold class A? |
| `core.ClassBChange` | UFO role | the proposal, the rule that classifies it, who applied it | Which class rule makes this proposal hold class B? |
| `core.ClassCChange` | UFO role | the proposal, the rule that classifies it, who applied it | Which class rule makes this proposal hold class C? |
| `core.EvidenceRole` | UFO role | the record, the claim it is offered for or against, who offered it | Which claim is this record evidence for? |
| `core.SocialRole` | UFO role | the player, the relation that makes it true, the rule that defines it | Which relation makes this player hold the role? |
| `core.ConsentState` | UFO situation | the round, its proposal, every objection with its disposition | Does consent exist if nobody was asked? No. |
| `core.Driver` | UFO situation | what is happening, its effect, why it matters | Can you point to it happening? You must be able to. |
| `core.Exception` | UFO situation | the rule, the scope, the justification | Does the rule still hold outside the scope? Yes. |
| `core.Relief` | UFO situation | the rule, its owner who granted the relief, scope, ledger entry; the granting is an authorization | Does the rule change? No. |
| `core.VerificationVerdict` | UFO situation | the verification that produced it, the requirement or DoD row, the criteria | Which check produced it, and has a later one superseded it? |
| `core.Waiver` | UFO situation | the requirement, its waiver authority, scope, expiry | Does the commitment change? No. |

## Open

These concepts carry no category yet. Each needs a decision, or a split, first.

| Concept | Why it is open |
|---|---|
| `core.Action` | A planned step with owner and date mixes an action type (a plan) and a commitment to carry it out (a closed appointment, UFO-C). Decide which the word names. |
| `core.CommitmentBaseline` | An identity question: a set replaced on every change (a record), or one baseline that changes under control. The agreement on it is a relator. |
| `core.Configuration` | A control regime: rules plus the change authorities' powers. Decide whether the word names the regime or the controlled set. |
| `core.Variance` | A comparison of two values of one quality (plan figure and actual): a formal relation, not one of the meta-categories. |
| `core.Direction` | The owner's goals (propositions) and AK's record of them. Decide which the word names. |
| `core.Readiness` | A phase if ready and not ready partition an item's life; otherwise a situation. |
| `core.DominantConstraint` | A role a requirement plays relative to one design; it needs the design relation first. |
| `core.OrganisationModel` | A conceptual artefact (Binner's metamodel); categorising it adds nothing for governance records. |
| `core.ConsentTier` | A tier of paths by who must consent (Core, Org, Project). It is not the decision class, which is `core.DecisionClass` since AK 6364; its own category is a separate question. Reserved identifier. |
| `core.Observation` | Overloaded: the measurement event and its record. A split candidate. |
| `core.Verification` | Deprecated on 2026-09-27; use core.VerificationEvent. See `ontology/decisions/2026-09-27-governance-core-splits.md`. |
| `core.Consent` | Deprecated on 2026-09-27; use core.ConsentState. See `ontology/decisions/2026-09-27-governance-core-splits.md`. |
| `core.Role` | Deprecated on 2026-09-27; use core.SocialRole. See `ontology/decisions/2026-09-27-governance-core-splits.md`. |
| `core.Capability` | Deprecated on 2026-09-27; use core.ActorCapability. See `ontology/decisions/2026-09-27-governance-core-splits.md`. |
| `core.Evidence` | Deprecated on 2026-09-27; use core.EvidenceRole. See `ontology/decisions/2026-09-27-governance-core-splits.md`. |

## Checks this model allows later (warn-only, ADR-0008 §10)
- A concept with a role category and no relation that makes the role true.
- A relator with fewer than two parties.
- An event concept with phases or a status that changes.
- Sibling phases not declared as a partition.
- A rigid concept (kind) that is_a an anti-rigid one (role, phase).
- A description that names two categories ("the act and outcome").

## Sources
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1): pp. 170–175 and Fig. 1, read on the page images on 2026-09-27.
- Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C): §2–§4 and Figs. 1–3, read on the page images on 2026-09-27.
- The research note behind the adjudication's school 7 (session-local, 2026-09-26), for Guizzardi's thesis (2005), UFO-L (Griffo, Almeida, Guizzardi 2018) and the per-term analysis.
- Controlled-vocabulary adjudication, addendum: governance-kernel `docs/project/2026-09-26-controlled-vocabulary-adjudication.md`.
- R. Guizzardi, Carneiro, Porello, G. Guizzardi (2020), A Core Ontology on Decision Making, ONTOBRAS 2020, CEUR-WS 2728, pp. 9–21: §3 and Fig. 2, read on 2026-10-02 in the text of the CEUR-WS copy.
- Carvalho, Almeida, Fonseca, Guizzardi (2017), Multi-level ontology-based conceptual modeling, Data & Knowledge Engineering 109, pp. 3–24: categorization, partitions, Fig. 5; and Fonseca, Guizzardi, Almeida, Sales, Porello (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607, pp. 18–34: axiom a7, Fig. 3, §4.4. Both read on 2026-10-02 in the text of the authors' copies (NEMO, UFES), not the page images.
