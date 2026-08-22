---
ont:
  id: "core.Receipt"
  type: concept
  labels: ["Receipt"]
  synonyms: []
  description: "Durable, integrity-checkable record binding an action or artifact to actor, time, and content digest."
  relations: []
  examples:
    - "A release evidence archive plus checksum attached to an immutable tag"
    - "A custody record binding an evidence closure to a task ID and revision"
  anti_examples:
    - "An editable log line with no content digest"
    - "A promise to write the record down later"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Receipt (core.Receipt)

## Definition
Durable, integrity-checkable record binding an action or artifact to actor, time, and content digest. A receipt establishes custody and lineage — that the recorded thing existed, in this form, at this time, under this actor.

## Typical usage
- Proving an artifact was retained byte-for-byte (checksums alongside archives).
- Anchoring lineage for audits, recovery decisions, and later reviews.

## Common confusions
- Confused with verification: a receipt proves presence and integrity of bytes; it says nothing about whether those bytes are correct, safe, or meaningful.
- Confused with authority: recording who did something does not establish that they were allowed to.
- Custody is not causality: holding a receipt for X does not prove X caused anything.
