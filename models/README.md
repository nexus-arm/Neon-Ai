# Models

The `models/` directory tracks the curated models available for the cybersecurity-enhanced deployment.

- Update `model_list.yaml` when adding or deprecating models so the deployment tooling can stay in sync.
- Store small metadata files here; large binaries should be downloaded during deployment or mounted via volumes.
- Keep quantization and version notes alongside each entry to avoid ambiguity between environments.
