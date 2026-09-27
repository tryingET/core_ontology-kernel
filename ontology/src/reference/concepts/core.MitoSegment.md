---
ont:
  id: "core.MitoSegment"
  type: concept
  labels: ["MITO segment"]
  synonyms: ["segment"]
  description: "One of the five places in Binner's MITO control loop (Führung, Input, Transformation, Output, Leitung) where a process step, record or document sits."
  relations: []
  examples:
    - "A process standard whose front matter lists mito_segments: [Führung, Input]"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# MITO segment (core.MitoSegment)

## Definition
One of the five places in Binner's MITO control loop (Führung, Input, Transformation, Output, Leitung) where a process step, record or document sits.

## Typical usage
- Docs record their segments in front matter as mito_segments.
- The FCOS cockpit places coordination items by segment.

## Common confusions
- Not the retired placement layers, not a NASA product layer, not an architecture layer (Layer-N).

## Source and mapping
- MITO model definition: the loop has five segments (B1 pp. 24, 55; B2 pp. 131–132); Binner also draws a four-segment variant with one Management roof.
- Owner decision D13 (2026-09-26): MITO structure words belong to the core.
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.

Admitted: AK task 6147, 2026-09-27
