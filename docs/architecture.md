# Architecture Overview

This document sketches the structure of the Neon-Ai deployment and how the pieces in this repository are meant to fit together.

## Core Components
- **Deployment tooling**: `deploy/deploy_cybersec_enhanced.py` drives setup (Docker install, Open WebUI + Ollama bootstrap, and model selection).
- **Container specs**: `deploy/docker/Dockerfile` and `deploy/docker/docker-compose.yml` describe how to run the services in containers.
- **Application layer**: `src/` hosts entrypoints, orchestration helpers, and future service code for custom extensions.
- **Models registry**: `models/model_list.yaml` lists curated cybersecurity-focused models that can be pulled or mounted.
- **Configuration**: `src/config/default.yaml` holds runtime defaults; `src/config/security_policy.yaml` documents security baselines.
- **Observability**: `deploy/scripts/monitor.sh` offers a minimal health check scaffold; extend it to include metrics and alerts.

## High-Level Flow
1. Operators run `python deploy/deploy_cybersec_enhanced.py` (or invoke it via Docker/CI).
2. The script ensures Docker is available, applies security posture defaults, and pulls the requested models.
3. Compose definitions start the services (Open WebUI UI layer + Ollama runtime) and mount model data from `models/`.
4. Application helpers in `src/modules/` can be wired into the containers to coordinate model management or expose APIs.

## Security Pillars
- **Isolation**: Prefer containerized execution via Docker/Compose; keep model storage in dedicated volumes.
- **Network controls**: Restrict exposed ports to what is documented in `docker-compose.yml`; enforce firewall rules per `security_policy.yaml` guidance.
- **Integrity**: Pin image tags and model versions in `model_list.yaml`; verify checksums where possible.
- **Observability**: Add log shipping, uptime checks, and resource monitoring hooks inside `deploy/scripts/monitor.sh`.

## Next Steps
- Replace the placeholder Dockerfile/Compose definitions with environment-specific builds.
- Wire tests under `tests/` to validate deployments and model availability.
- Document threat models and hardening steps inline with the security policy.
