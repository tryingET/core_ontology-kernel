---
summary: "AK 6364 decision packet (revised after independent review): the ontology questions AK 5991's decision records routed to ontology-kernel. It covers the raised argument versus objection versus concern, when dissent exists, the missing core.Decision and its taxonomy, refusal and revocation, the decision class (which is not core.ConsentTier), whether a permission lapses, and S3 concerns. Each has options and a recommendation, and the packet lists every in-place-or-new-identifier ruling, draft concept texts, the class-C records and each consumer's follow-up."
read_when:
  - "Before the Holding Owner decides AK 6364."
  - "When a record or schema uses core.Objection, core.Dissent, core.Authorization, core.ConsentTier, core.ConsentRound, core.Permission, or a word for decision, decision class, refusal, revocation or concern."
type: "project"
---

# Ontology questions from AK's decision records (AK 6364)

## 1. What is asked, and of whom

**Driver.** AK 5991 built AK's own records for a consent round, an authorization and a dissent (schema 47,
dormant on main since 2026-10-01). It keyed every row to an ontology-kernel identifier. Some questions
arose that AK may not answer itself, because meaning is ontology-kernel's to define. AK recorded an
interim representation for each and routed them here (agent-kernel
`docs/project/2026-10-01-ak5991-decision-consent-authorization-dissent-design.md` §7). One of them
overlaps the inspector's finding N6 on v0.3.0 (inspection AK 6188, evidence 11290, carried by AK 6218).

**Who decides.** The questions touch:
- reserved identifiers: `core.Objection`, `core.Dissent`, `core.Authorization`, `core.ConsentTier`,
  `core.ConsentRound`, `core.Permission`, `core.DecisionRecord`;
- the core word *decision*, which only the Holding Owner defines (ADR-0008 §1.5).

The decision is therefore class C: the Holding Owner decides after the consent round ADR-0008 §4
prescribes (§6 below).

**Identifier stability.** v0.3.0 released these identifiers, and CORE-INV-002 says "meaning changes use
deprecation + new ID". The in-place corrections of 2026-09-28 (AK 6167) were allowed only because those
identifiers had never been released. So for every wording change below, the owner rules: **in place**
(the owner reads it as a clarification that keeps the extension) or **new identifier**, with the old
one deprecated. §5 lists each such ruling, with the consumer evidence. This packet recommends and does
not rule.

**Deadline.** 2026-10-31. The FCOS pilot's delegation expires the same day (ADR-0008 §6).

## 2. Summary of recommendations

| # | Question | Recommendation |
|---|---|---|
| 1 | What is an argument that fails the objection test? | Name the raised argument, S3's *possible objection*. The test decides whether it is an objection. If it fails, it is not an objection, though it may reveal a concern (Q7). |
| 2 | When does dissent exist, and is *overruled* an end state? | One end-state set: integrated, withdrawn, standing. Dissent exists once a decision has gone ahead over a standing objection. Before that, the objection is *escalated*. |
| 3 | Which concept is "the decision that went ahead"? | Follow Guizzardi's *Core Ontology on Decision Making*. A decision is an **intention** (a mode) created by a **deliberation** (an act) and manifested in a **decision-resulting action**. Authorization, refusal and revocation are such actions; a decision gate is a deliberation. |
| 4 | Are a refusal and a revocation authorizations? | No. They are acts of their own: decision-resulting actions beside `core.Authorization`, which stays the grant. |
| 5 | What is the decision class, and is it `core.ConsentTier`? | It is **not** ConsentTier. Following Guizzardi's multi-level theory, the decision class is a **type of types**: it categorises proposed changes into class-A, B and C change, each a role. "Autonomy level" is a different concept on the agent's side (delegated capacity), for later. |
| 6 | Does a permission lapse? | It may end at a time its authorization states. A review date ends nothing. |
| 7 | Do S3 concerns get an identifier? | Yes, `core.Concern`. |

## 3. The questions

### Q1. An argument that fails the objection test

**Kernel today.**
- `core.Objection` (mode): "A reasoned concern that blocks consent until addressed". Its anti-example
  is "A preference without impact/risks".
- `core.ConsentRound`: "each objection is tested as an argument".
- Nothing names what is raised before the test, or the result when an argument fails it.

**What the sources say.**
- **S3** distinguishes three things.
  - A *possible objection* is an argument raised for changing something.
  - An *objection* is "an argument … that reveals consequences or risks that are preferably avoided for
    the organization, or that demonstrates worthwhile ways to improve".
  - A *concern* is "an assumption that cannot (for now at least) be backed up by reasoning or enough
    evidence to qualify as an objection to those who are considering it".

  An argument is tested. If it qualifies, it is an objection to resolve. Otherwise "not all arguments
  raised are objections, but they **might reveal** concerns" (emphasis added): a failed argument may
  be a preference or a misconception, and is then neither. The line "is sometimes dependent on
  context" (S3 practical guide, local edition
  `holdingco/governance-kernel/external/s3-0-practical-guide`, v2024-04-18a: *Objections*; *Test If Arguments
  Qualify as Objections*; `glossary.yaml`; that snapshot was removed on 2026-10-08, and the current v2026-01-26 notes
  are in `~/Documents/Obsidian/Wiki/S3/`).
- **The adjudication and consent-change-control** speak of "qualified objections" and "how each was
  tested". **ADR-0008 §8** lists concerns in the class-B consent record.
- **FCOS** (`fcos.consent-record.v1`) puts every raised argument in `objections`, with a disposition
  that includes `not_valid`.
- **AK 5991** records every raised argument in `decision_objections`, keyed `core.Objection`, with a
  separate `qualification` (`qualified` | `not_qualified`). Only a qualified standing objection
  blocks consent.

**Options.**
- (a) A failed argument is still an objection, with a fourth disposition. This is FCOS's `not_valid`,
  and it contradicts the kernel's own anti-example.
- (b) A failed argument is not an objection, and the test result is recorded on the raised argument.
  This needs a name for what is raised: S3's *possible objection*. The objection is then a possible
  objection that qualified. A concern found along the way is recorded on its own (Q7).
- (c) Binary: a failed argument is a concern. Rejected: S3 says only that it *might reveal* one.
- (d) Leave it to each layer. That is what produced three vocabularies.

**Recommendation: (b).** It is S3's structure, and AK's interim representation already has its shape:
a raised row plus a test result. Under (b):
- admit `core.PossibleObjection` (label "possible objection") for the raised argument;
- `core.Objection` becomes "a possible objection that qualified". Whether that is in place or a new
  identifier is a §5 ruling;
- `core.ConsentRound` reads "each possible objection is tested as an argument" (a §5 ruling).

### Q2. When does dissent exist, and how does an objection end?

**Kernel today.** There are three wordings:
- `core.ConsentRound`: an objection ends "integrated, withdrawn or standing";
- the reference model's question for `core.Objection`: "standing, integrated, withdrawn or overruled?";
- `core.Dissent`: "an objection still standing when the owner authorized the change anyway", with the
  diagnostic "Does dissent exist without a decision that went ahead? No."

**But the adopted governance texts use *dissent* earlier:**
- consent-change-control: dissent is "qualified objections that were overruled **or stayed
  unresolved**", and "authorization … with the dissent in view";
- ADR-0008 §4: "unresolved objections reach the owner **as dissent**";
- the adjudication: "preserved and escalated … shown to whoever authorizes".

**Options.**
- (a) Keep the ontology's sense. Dissent exists only once a decision has gone ahead over a standing
  objection. Before that, a standing objection that reached the authority is an *escalated objection*,
  and the governance texts change their wording (class C in governance-kernel).
- (b) Adopt the governance texts' sense. Dissent exists from the moment a qualified objection stays
  unresolved, and is kept with the decision whichever way it goes. That changes `core.Dissent`'s
  meaning, so it needs a new identifier, and a refused decision then carries "dissent" against nothing.

**Recommendation: (a).** It is the later, ontology-delivered meaning, which is the vocabulary
authority, and AK already implements it (`escalated_objections` before a grant). Under (b), a refusal
would carry dissent from an outcome that agreed with the objector. In both options:
- one end-state set: **integrated, withdrawn, standing**;
- *integrated* means resolved by any amendment S3 lists, including deferring the objection with an
  owner and a date, or leaving the proposal unchanged while monitoring;
- *overruled* is not a state; it is a standing objection over which a decision went ahead;
- a possible objection that did not qualify, and a concern, never become dissent.

**Wording changes under (a):**
- the reference model's question for `core.Objection`: "Has it ended integrated, withdrawn or
  standing, and did a decision go ahead over it?";
- `core.Dissent`'s typical usage: "before a decision, a standing objection is escalated, not yet
  dissent" (a §5 ruling, given the synonym "recorded disagreement");
- in governance-kernel: consent-change-control, ADR-0008 §4 and the adjudication's wording (class C).

### Q3. "The decision that went ahead": what a decision is

**Kernel today.**
- `core.Dissent` requires "the decision that went ahead over it".
- `core.DecisionRecord` requires "the decision and its consent, authorization and dissent records".
- `core.DecisionGate` is "an act: a named authority decides, against criteria set in advance, whether
  work may proceed".
- `core.Goal` is a proposition, "the agent whose intention it is".
- No concept is the decision, and none is an intention or a deliberation. *decision* is a core word
  whose definition is the Holding Owner's (ADR-0008 §1.5).

**What Guizzardi says.** UFO's authors have a core ontology for exactly this (R. Guizzardi, Carneiro,
Porello, G. Guizzardi, "A Core Ontology on Decision Making", ONTOBRAS 2020, CEUR-WS 2728).
- **Decision.** "A DECISION is an INTENTION created by a DELIBERATION." An intention is a mental moment,
  a UFO mode, which "is the world as the AGENT commits to bringing about by executing ACTIONS". Its
  propositional content is a goal.
- **Deliberation.** It is the action that creates the decision. An agent performs it "due to a certain
  (motivating) INTENTION", weighing alternatives by preference and criteria.
- **Manifestation.** The decision "can eventually manifest in the performing of another ACTION termed a
  DECISION RESULTING ACTION, whose result is termed a CONSEQUENCE", a situation. "A DECISION is thus
  associated to two ACTIONS": a creation with respect to the deliberation, and a manifestation with
  respect to the resulting action.
- **Criterion.** A criterion is a quality type or mode type the agent takes into account (for example
  price or efficiency), not a mental moment.
- **Documentation.** The paper's own application is decision documentation. Its template is the
  motivating intention, the intentions by priority, the alternatives, each criterion and its value,
  and the decision. That is `core.DecisionRecord`'s job.

**Mapped onto the governance core:**
- the **decision** is the decider's intention: a mode, not an event;
- a **deliberation** is the act of deciding. `core.DecisionGate` is a deliberation by a named authority
  against criteria set in advance;
- **authorization, refusal and revocation** are decision-resulting actions. They are institutional
  acts: they create, withhold or end a permission (UFO-L: a legal relation with the permission as a
  position in it);
- "**the decision that went ahead**" over a standing objection is a decision whose resulting action
  happened while the objection stood. AK's dissent points at that action (the grant), which
  manifests the decision;
- the paper is about an individual agent's decision. It leaves "social capacities (acquired through
  delegation relations)" to future work, so collective decision making beyond this mapping is not
  covered.

**Options.**
- (a) Follow the decision-making ontology: admit `core.Decision` (mode, an intention) and
  `core.Deliberation` (event, `produces core.Decision`). `core.DecisionGate is_a core.Deliberation`.
  Authorization, refusal and revocation relate to the decision they manifest.
- (b) The earlier draft of this packet: a decision as the umbrella act. Guizzardi's analysis rejects
  this: it collapses the intention, the deliberation and the resulting act into one.
- (c) No `core.Decision` now: `core.Dissent` points at the authorization that went ahead.

**Recommendation: (a).** It is the published UFO analysis, and it keeps three things apart: what the
decider intends, the act of deciding, and the act that carries the decision out. This is the same
discipline the kernel already applies elsewhere (the AK 5987 splits).
- **New relation type.** The kernel has no relation for *manifests* (UFO-B manifestation). Add one, or
  use `depends_on` until it exists. Either way it is a ruling.
- **AK's `decisions` row** is neither the intention nor an act: it has a workflow state. AK qualifies
  its label ("decision case", ADR-0008 §1.3) and maps it to `core.DecisionRecord`.

### Q4. Refusal and revocation

**Kernel today.**
- `core.Authorization`: "an act: a sign-off … which grants a permission". A revocation "is a new
  event", but nothing names it.
- The adjudication records `granted | declined | not_required`. ADR-0008 §8 records `granted` or
  `declined`.
- FCOS's revocation facts carry no `ontology_ref`: "the core has no concept for that".
- AK 5991 puts `core.Authorization` on its grant, decline and revoke rows alike.

**Options.**
- (a) Widen `core.Authorization` to "grants or refuses". That is a new identifier, and the grant
  loses its own.
- (b) Two acts of their own: a refusal founds no permission, and a revocation ends one. Under Q3(a)
  both are decision-resulting actions, like the grant.
- (c) An authorization *record* (a kind, like Dissent) holding an outcome: a grant, a refusal or not
  required.

**Recommendation: (b), with (c) as the record shape.**
- The acts need identifiers so that rows can key to them.
- The "authorization" part of `core.DecisionRecord` then holds a grant, a refusal or "not required",
  where "not required" follows from the decision class (Q5).
- **Labels:** *refusal* (synonym "declined authorization"). For *revocation*, since revoking a
  *delegation* ends an authority rather than a permission, the owner chooses between:
  - one concept covering both ("ends a permission or an authority an earlier act founded"); or
  - a qualified label for each (*permission revocation*, *delegation revocation*).

### Q5. The decision class, which is not `core.ConsentTier`

**Kernel today.** `core.ConsentTier` (reserved): "A governance tier defining who must consent for a
change". Its example is "Kernel tier requires holding owners; project tier requires project owners". It
has no category.

**Evidence that the two differ.**
- consent-change-control keeps consent **tiers by path** (Core / Org / Project) apart from **decision
  classes** A / B / C. Its MR template asks for both.
- On 2026-09-30 the Holding Owner asked (evidence 11507): "the decision class is that really a
  ConsentTier? or not something different? like AutonomyLevel or something like this?".
- AK 5991's design note made the same conflation; it is corrected in agent-kernel.

**What a decision class is.** A class is assigned by applying the class rules to a proposed change:
- class C: the Holding Owner's scope, plus anything that cannot be made reversible;
- class B: reversible changes that reach several domains, and one-way changes once made reversible;
- class A: reversible, one domain.

A change can move between classes, for example when it is made reversible.

**What Guizzardi says.** His multi-level theory (MLT, with Carvalho, Almeida and Fonseca), built into
UFO and OntoUML 2, separates two levels. Sources: Carvalho, Almeida, Fonseca, Guizzardi,
"Multi-level ontology-based conceptual modeling", DKE 109 (2017), pp. 3–24; Fonseca et al.,
"Incorporating Types of Types in Ontology-Driven Conceptual Modeling", ER 2022, LNCS 13607, pp. 18–34.
- **The classes are types, at the first level.** "Class-A change", "class-B change" and "class-C
  change" are types whose instances are individual changes. They are anti-rigid, since a change can
  leave one class for another.
  - The test for which anti-rigid type: a **phase** is entered through an intrinsic change of its
    bearer, while a **role** holds through a relation.
  - Here membership depends on the domains the change reaches and on the class rules, so each class is
    a **role**.
- **"Decision class" is a type of types, one level up.** Its instances are those three types, not
  changes. MLT calls this a **high-order type** that *categorises* the base type, the powertype
  pattern. Examples from the papers: *Species*, whose instances include *Emperor Penguin* and *Dog*
  (Fonseca et al. 2022, Fig. 3); *Person Role*, with instances *Manager* and *Researcher*, which
  categorizes *Person* (Carvalho et al. 2017, Fig. 5).
- **Quality is the wrong category.** A quality takes a value in a quality space and is intrinsic to its
  bearer; a class is a classification by rule.
- **"Autonomy level" names something else.** It describes how far an *agent* may decide without the
  owner: a property of the agent's delegated capacity. The decision-making ontology defers this to
  "social capacities (acquired through delegation relations)". It is the counterpart of the decision
  class, not another name for it. A class-C change is one that no delegated capacity below the Holding
  Owner covers.

**Options.**
- (a) Model it as MLT does:
  - admit the three class roles and `core.DecisionClass` as a high-order type that categorises proposed
    changes;
  - add *high-order type* to the reference model's categories, which is a foundational-category
    ruling;
  - leave autonomy level for when delegation is modelled.
- (b) Admit only the three class roles. "Decision class" then names their partition in prose, with no
  identifier.
- (c) A single concept with category quality or role. Guizzardi's analysis rejects this as mixing the
  two levels.

**Recommendation: (a).** It is the published account and keeps the levels apart. If the owner wants no
new foundational category yet, (b) is the safe subset; (a) can follow.
- `core.ConsentTier` stays unchanged. It is the path-based tier, and its category is a separate,
  later question.
- Which records each class requires stays governance-kernel's and the owner's (AK 6366).

### Q6. Does a permission lapse?

**Kernel today.**
- `core.Permission`: "What a party may do within a stated scope, granted by an authorization or by a
  rule".
- `core.Waiver` records name an expiry.
- `core.AgreementReview` ends in keep, evolve or drop.

**Sources.**
- FCOS's grant carries `not_after`, which it describes as "the agreement review date" and enforces as
  an end.
- The independent review of AK 5991 recorded that AK's draft copied that field and "coined an expiry";
  AK dropped it.

**Options.**
- (a) No lapse; only a revocation ends a permission.
- (b) A permission may end at a time its authorization states as part of the scope, and then ends
  without a revocation. The review date is separate and ends nothing.
- (c) The review date ends it.

**Recommendation: (b).** Bounded permissions are ordinary, and waivers already carry an expiry. A review
that ends in *drop* is followed by a revocation. This changes `core.Permission`'s typical usage ("its
scope may say when it ends"), which is a §5 ruling.

### Q7. S3 concerns

Admit `core.Concern`.
- S3: concerns "don't prevent proposals becoming agreements", but they lead to amendments, evaluation
  criteria and review dates.
- ADR-0008 §8 already requires class-B consent records to hold them.
- A concern is not dissent (Q2), and a failed possible objection is not automatically a concern (Q1).

## 4. Draft concept texts

These are the packet's earlier drafts. The concept files and
`ontology/decisions/2026-10-02-decision-records-questions.md` carry the later wording from rulings
12302 and 12346 and the consent-round integration. Each draft follows ontology-markdown-v1 and the
reference model: one category with its required relata, a source, and a reference-model row with its
diagnostic question.

**`core.PossibleObjection`** ("possible objection")
- **Description:** "An argument a party raises against a proposal, agreement or activity, offered as
  an objection before it is tested."
- **Category:** UFO mode (`instance_of core.UfoCategory.Mode`), held by the party.
- **Required relata:** who raised it, the proposal, agreement or activity, the argument, the test and
  its result.
- **Source:** S3 *Test If Arguments Qualify as Objections*.
- **Diagnostic question:** "Has it been tested, and did it qualify?"

**`core.Objection`** (rewording; §5 ruling)
- **Description:** "A possible objection that qualified: the party's argument reveals consequences or
  risks preferably avoided, or a worthwhile improvement. It blocks consent until it is integrated or
  withdrawn."
- **Category:** UFO mode; the argument is its content, not a second category.
- **Relations:** `is_a core.PossibleObjection`.
- **Source:** S3 glossary *objection*.

**`core.Concern`**
- **Description:** "An assumption a party holds about a proposal, agreement or activity that cannot,
  for now, be backed by enough reasoning or evidence to qualify as an objection to those considering
  it. It never blocks consent."
- **Category:** UFO mode.
- **Required relata:** who holds it, the proposal, agreement or activity, the assumption.
- **Source:** S3 glossary *concern*.
- **Diagnostic question:** "Could it block consent? Never."

**`core.Decision`** (the owner's word; after the decision-making ontology)
- **Description:** "A mode: the intention a decider forms by deliberating, whose content is the
  alternative chosen (doing nothing included) and which the decider commits to bring about."
- **Category:** UFO mode (an intention).
- **Required relata:** the decider (its bearer), the goal it commits to, the deliberation that created
  it, the alternatives and criteria weighed.
- **Source:** R. Guizzardi et al. 2020, §3.

**`core.Deliberation`**
- **Description:** "An act: an agent weighs alternatives against criteria and preferences and so
  creates a decision."
- **Category:** UFO event (an action).
- **Relations:** `produces core.Decision`.
- **Required relata:** the agent, the motivating intention, the alternatives, the criteria, the
  decision created.
- **Source:** R. Guizzardi et al. 2020, §3.
- **New edges in other files:**
  - `core.DecisionGate is_a core.Deliberation`;
  - `core.DecisionRecord depends_on core.Decision`;
  - `core.Dissent depends_on core.Decision`;
  - `core.Authorization`, `core.Refusal` and `core.Revocation` each `manifests` (or, until that relation
    exists, `depends_on`) `core.Decision`.

**`core.Refusal`**
- **Description:** "An act: the holder of the authority refuses a permission that was asked for; the
  proposal returns to its driver."
- **Category:** UFO event.
- **Relations:** `depends_on core.Authority`.
- **Required relata:** the refuser, the party refused, what was asked for, the basis.
- **Source:** adjudication clash 5.

**`core.Revocation`** (the label is the owner's choice, per Q4)
- **Description:** "An act: the holder of the authority ends one or more permissions that earlier
  authorizations founded; the authorizations stay on record."
- **Category:** UFO event.
- **Relations:** `depends_on core.Authority`. The edge `core.Authorization precedes core.Revocation`
  goes in Authorization's file.
- **Required relata:** the authorizations it ends, the revoker, the basis.
- **Source:** reference-model row for `core.Authorization`.

**The decision class** (after MLT; option (a) of Q5)
- **`core.ClassAChange`, `core.ClassBChange`, `core.ClassCChange`.** Each is "A role a proposed change
  plays under the class rules: …" (one line per class, from consent-change-control).
- **Category:** UFO role.
- **Required relata:** the change, the rule that classifies it, who applied it.
- **`core.DecisionClass`.** "A high-order type that categorises proposed changes; its instances are
  the three class roles; a change holds exactly one at a time."
- **Category:** high-order type, a new reference-model category (MLT).
- **Sources:** consent-change-control; the adjudication §6; Carvalho et al. 2017; Fonseca et al. 2022.

**`core.Permission`** (typical-usage line; §5 ruling)
- "Its scope may say when it ends; it then ends without a revocation. An agreement review date does
  not end it."

**ADR-0008 data file** (governance-kernel, class C):
- reserve the new identifiers;
- add *possible objection*, *concern*, *refusal*, *revocation* and the decision-class word to
  `core_words`, so that no lower layer defines them (§1.5).

## 5. The owner's rulings

1. **Q1.**
   - Admit `core.PossibleObjection` and `core.Concern`.
   - Reword `core.Objection` **in place or as a new identifier**. Consumer evidence: AK keys its
     not-qualified rows to `core.Objection` today, and FCOS lists `not_valid` arguments under
     `objections`. Both would move those rows to `core.PossibleObjection`.
   - `core.ConsentRound`'s "each objection is tested" becomes "each possible objection is tested":
     **in place or new**.
2. **Q2.**
   - Option (a) or (b).
   - Under (a), `core.Dissent`'s typical-usage line: **in place or new**, given its synonym "recorded
     disagreement".
   - The governance-kernel wording changes (class C).
3. **Q3.**
   - Option (a): the decision as an intention, per the decision-making ontology, or (c).
   - The owner's wording of `core.Decision`.
   - A `manifests` relation type, or `depends_on` meanwhile.
4. **Q4.** `core.Refusal` and `core.Revocation`, and whether revocation also covers delegations.
5. **Q5.**
   - Option (a): the three class roles plus `core.DecisionClass` as a high-order type, which adds the
     high-order-type category; or option (b): the roles only.
   - Leave `core.ConsentTier` unchanged.
   - Autonomy level later, with delegation.
6. **Q6.** Option (b), and `core.Permission`'s line: **in place or new**.
7. **Release.** The adopted changes go into v0.4.0, which the owner publishes.

### Rulings given so far

- **2026-10-01, Q1: possible objection** (option b; evidence 12130).
- **2026-10-01, Q2: dissent only after a decision went ahead** (option a; evidence 12130).
- **2026-10-01, Q3: follow the decision-making ontology** (option a): `core.Decision` is an intention
  created by `core.Deliberation`.
- **2026-10-01, Q5: full MLT** (option a): the class roles plus `core.DecisionClass` as a high-order
  type.
- **2026-10-01, Q4: refusal and revocation separate;** one revocation concept covers both permission and
  delegated authority.
- **2026-10-01, Q6: a permission may end at a time its authorization states;** a review date ends
  nothing.
- Q3 to Q6: evidence 12179.
- **2026-10-02, in place** (evidence 12209): the `core.ConsentRound`, `core.Dissent` and
  `core.Permission` changes keep their identifiers; prepare v0.4.0.
- **2026-10-02, `core.Objection` in place** (evidence 12211), after the owner asked for Guizzardi's
  view on type identity.
- **2026-10-02, the class roles' base type and `core.Decision`'s wording** (evidence 12302): each
  class role `is_a core.Proposal`; the owner adopted the drafted `core.Decision` text verbatim,
  "doing nothing included" with it.
- **2026-10-02, after the consent round** (evidence 12346; round 12306, tests 12312 and 12313): a
  possible objection may be withdrawn before its test, and one that fails is kept with its test result
  and may still be taken up; a proposal may be unclassified, and then no decision on it may go ahead;
  one decision record may document several decisions in order; AK amends migration 47.
- **2026-10-03, the remaining semantic points and early closure** (ruling 12461; closure 12462): keep
  `core.DecisionGate is_a core.Deliberation` and make its diagnostic name the decision formed; add
  `core.DecisionClass is_a core.UfoCategory.Role`, retaining HighOrderType. The owner closed the
  round early after both sources confirmed no objection standing (12349, 12351).
- **2026-10-03, final authorization** (12507): the owner authorized v0.4.0 content at
  `6a429bb7e1087553f4572009a743ca3b911f22ab`, including the disclosed in-place ConsentRound and
  DecisionRecord readings, Deliberation's “a decider” and the 2027-04-01 review date. It separately
  authorizes the four consumer queue bindings and push/preparation PR. Consumer receipt 12508
  binds 6368 and new owner tasks 6492–6494. Release publication remains the owner's separate act.
- Release prep is under way: the change is drafted in
  `ontology/decisions/2026-10-02-decision-records-questions.md`; the owner authorizes the final
  content and publishes the release.

## 6. Records of this decision (class C)

- **Route (ADR-0008 §4).** Reserved identifiers and foundational categories go to the Holding Owner
  after the *stewardship* consent round. The stewardship roles are not held yet (5985), and during the
  pilot the owner answers consent rounds for the FCOS layer (§6). Every holder asked is therefore the
  Holding Owner, as for ADR-0008 itself ("No consent round was held: every affected layer is held by
  the Holding Owner today").
- **Objection sources.** Agents are objection sources, not holders (adjudication clash 2). The FCOS
  pilot session and the AK session are invited to raise possible objections, blind and in parallel,
  within a stated window. Each is tested, and concerns are kept.
- **Records** (ADR-0008 §8, class C):
  - consent;
  - the Holding Owner's authorization (grant or refusal), with any escalated objection in view;
  - dissent;
  - the conformance receipt for the exact corpus;
  - the driver (this packet, AK 6364);
  - a review date.

  They live in AK evidence until AK's schema-47 records are live (AK 6367), which waits for migration
  47 to carry the corrected keys (evidence 12346). After that, this decision can be the first to use
  them: an AK decision case for 6364, a consent round, and the owner's
  `ak decision authorize`.

## 7. What each consumer changes afterwards

| Consumer | Change | Owner |
|---|---|---|
| ontology-kernel | concept files, edges and reference-model rows (§4); a decision note under `ontology/decisions/`; v0.4.0; closes N6 (AK 6218) and adds the decision class to the reference model | Holding Owner |
| governance-kernel | the data file (reserved identifiers, core words); consent-change-control (dissent wording, MR template "Dissent" → escalated objections and dissent); human-on-the-loop-consent (`declined` → refusal); the ADR-0008 §4 and §8 wording; the vocabulary card's authorization / consent / dissent line | Holding Owner (class C) |
| org-handbook | the consent-tier SOPs stay on `core.ConsentTier`; class wording follows the decision class | Holding Owner |
| agent-kernel | `decision_objections` rows key to `core.PossibleObjection`; a qualified one is a `core.Objection`. `act` keys to Authorization, Refusal or Revocation. Concerns gain a home. The `decisions` row is labelled a decision case. An optional end on grants. Migration 47 is amended with these keys and a disposition grid matched to the final ConsentRound before any database holds it (evidence 12346; bound as AK 6471); after that, the append-only CHECK constants mean a forward migration with new rows or columns, never a rewrite. | agent-kernel |
| FCOS (pilot) | forward, in new record versions (v1 records, signed facts and archived inputs keep their v1 validators): `not_valid` arguments become possible objections that did not qualify, and leave `dissent`; new revocation records get the revocation identifier; `not_after` is the end its grant states, enforced as now, and a review ends nothing; `decision_class` (design D11) maps to the decision class | FCOS pilot holder |
| AK 6366 | waits on the decision-class concept, not on `core.ConsentTier` (corrected in AK) | Holding Owner, then agent-kernel |
| company and repo layers | repin to v0.4.0 (pi-extensions' `ontology/dist` resolves these identifiers) | each layer's holder |

## 8. If nothing is decided by 2026-10-31

- **AK** keeps its interim representation, which loses no fact.
- **FCOS and AK** keep different words for the same things.
- **AK 6366** stays blocked.
- **The FCOS pilot** delegation lapses unless the owner renews it.
- **The bootstrap Leitung review** on 2026-10-26 lists the open trigger.

## 9. Independent review

A reviewer with only the sources attacked the first draft. The verdict was "rework, targeted". Each
finding and what this revision did with it:

| # | Finding | Disposition |
|---|---|---|
| 1 | blocker: Q5 took `core.ConsentTier` for the decision class; the owner had already questioned that (11507) | Q5 rebuilt: separate concepts, ConsentTier untouched; the AK design note and 6366 corrected |
| 2 | Q5's category reasoning failed the reference model's tests; class C is a scope rule, not reversibility × blast radius | role recommended, quality and phase rejected with reasons; the class-C scope is quoted |
| 3 | Q1 dropped the "test result" option and misread S3 (a failed argument *might* reveal a concern) | possible objection (b) recommended; binary option rejected; S3 quoted in full; mappings fixed |
| 4 | the "clarify in place" claims were asserted, not put to the owner | §5 lists every in-place-or-new ruling with consumer evidence (Objection, ConsentRound, Dissent, Permission) |
| 5 | governance texts call unresolved objections "dissent" before a decision | Q2 now offers (a) and (b), recommends (a), and lists the class-C wording changes |
| 6 | the core.Decision draft also covered authorization, refusal and revocation without saying so; options missing; AK's decision row is not an act | Q3 explicit taxonomy (`is_a` edges); complex-event and authorization-record options added; AK "decision case" label |
| 7 | §6 named the wrong route and round members | stewardship route stated; the owner answers as holder; FCOS and AK sessions invited as objection sources |
| 8–9 | draft-text defects; reserved list and core words incomplete | relata, sources and diagnostic questions fixed; the Objection draft no longer names two categories; Permission and ConsentRound added; core words listed |
| 10–11 | §8 records and consumer table incomplete | conformance receipt, driver and review date; pilot expiry; consumer table extended |
| nits | quote attributions, N6 provenance, wording | fixed |

After the owner's question "what would Giancarlo Guizzardi say?" (2026-10-01), Q3 and Q5 were redone
from his published work. Q3 now follows the Core Ontology on Decision Making (a decision is an intention
created by a deliberation). Q5 now follows MLT (the decision class is a high-order type over the class
roles; autonomy level belongs to the agent's delegated capacity). The earlier "umbrella act" and
"role" recommendations are withdrawn.
