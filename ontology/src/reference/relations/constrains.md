---
ont:
  id: "core.rel.constrains"
  type: relation
  labels: ["constrains"]
  description: "Axiom/Constraint begrenzt oder gilt für X"
  group: "constraint"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "parents"
  examples:
    - "core.Policy constrains core.Repo (e.g. no-secrets policy applies to a repo)"
  anti_examples:
    - "Using constrains when you mean depends_on"
---

## Definition
`X constrains Y` means X limits Y by defining a rule/constraint/policy that applies to Y (scope/applicability).

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- A rule/constraint/policy limits a target (scope/applicability).

## Do not use when
- You mean a runtime/build dependency (use `depends_on`) or simple usage (use `uses`).

## Domain / Range
- Domain: `core.Constraint` / `core.Policy`
- Range: any constrained concept (commonly `core.Repo`, `core.Service`)
