# Core relation types (kernel)

These are the kernel relation types for all layers.
Company/Repo may propose extensions only via Decision + definitions + operational update.

Inverse policy:
- Kernel relations may specify `ont.inverse` only when the inverse relation label is also defined in the kernel.
- For now, only symmetric relations use `ont.inverse` pointing to themselves (e.g. `conflicts_with`, `similar_to`).
