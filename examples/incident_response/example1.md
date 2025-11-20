# Incident Response Example

This walk-through illustrates how to combine the curated models with Open WebUI during an incident response sprint.

1. Start the stack: `docker compose -f deploy/docker/docker-compose.yml up -d`.
2. Open WebUI and select `seneca-cybersecurity-q4` as the default helper.
3. Feed the model a log bundle or IOC list and ask it to summarize likely attack paths.
4. Switch to `cyberguard-7b` for SOC-style triage and detection rule suggestions.
5. Use `codeshield-7b` to review hotfixes or patches before rollout.

Document findings and playbooks under `docs/` so they remain close to the tooling.
