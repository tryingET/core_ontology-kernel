---
summary: "Schema: concept/relation front matter + deprecation fields."
read_when:
  - "When adding or changing ontology files"
  - "When implementing validators/builders"
---

# Ontology schema (kernel)

This repo uses Markdown files with YAML front matter.

## Common front matter

Required:
- `ont.id` (stable, globally unique within the holding)
- `ont.type` (`concept` or `relation`)
- `ont.labels` (short label list)
- `ont.description` (1-line definition)

Recommended:
- `ont.status`: `active` (default) or `deprecated`

### Deprecation

If `ont.status: deprecated`, include:
- `ont.deprecated.since` (date)
- `ont.deprecated.replaced_by` (new `ont.id`)
- `ont.deprecated.decision` (URL or repo path to decision record)

## Concept-specific

Required:
- `ont.relations`: list (use `[]` if none)

## Relation-specific

Optional:
- `ont.inverse`: only if the inverse relation label is also defined in the kernel (or the relation is symmetric and self-inverse).

