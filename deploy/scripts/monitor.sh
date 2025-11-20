#!/usr/bin/env bash
# Basic health-check scaffold for the Neon-Ai deployment.

set -euo pipefail

log() {
  printf '[%s] %s\n' "$(date +"%Y-%m-%dT%H:%M:%S%z")" "$1"
}

log "Inspecting running containers..."
docker ps --filter "name=neon" --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'

docker stats --no-stream || log "Docker stats unavailable (daemon down?)"
