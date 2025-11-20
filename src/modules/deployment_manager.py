"""Deployment orchestration placeholder.

Use this module to hook the Python runtime into Docker/Open WebUI automation or
CI pipelines. It currently logs the intended actions to keep the skeleton light.
"""

from __future__ import annotations

from modules.model_manager import ModelManager
from modules.utils import log


class DeploymentManager:
    def __init__(self) -> None:
        self.model_manager = ModelManager()

    def deploy(self) -> None:
        log("Starting deployment stub — replace with real orchestration steps.")
        default_model = self.model_manager.default_model()
        log(f"Default model: {default_model.name} ({default_model.role})")
        log(
            "Wire this method to the cyberpunk deployment script or Docker Compose\n"
            "definitions under deploy/."
        )

    def available_models(self) -> None:
        for entry in self.model_manager.list_models():
            log(f"- {entry.name} [{entry.role}] {entry.size}")
