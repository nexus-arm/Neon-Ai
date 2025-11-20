"""Simple model registry helper for Neon-Ai.

This stub reads from `models/model_list.yaml` when PyYAML is available;
otherwise it falls back to an inline catalogue so the rest of the code keeps working.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - placeholder behavior
    yaml = None


@dataclass
class ModelInfo:
    name: str
    role: str
    size: str
    source: str
    default: bool = False
    notes: Optional[str] = None


class ModelManager:
    def __init__(self, model_list_path: Optional[Path] = None) -> None:
        repo_root = Path(__file__).resolve().parents[2]
        self.model_list_path = model_list_path or repo_root / "models" / "model_list.yaml"
        self.models: List[ModelInfo] = self._load_models()

    def _load_models(self) -> List[ModelInfo]:
        if yaml and self.model_list_path.exists():
            data = yaml.safe_load(self.model_list_path.read_text()) or {}
            return [
                ModelInfo(
                    name=entry.get("name", "unknown"),
                    role=entry.get("role", "uncategorized"),
                    size=str(entry.get("size_gb", "")) + " GB" if entry.get("size_gb") else entry.get("size", ""),
                    source=entry.get("source", "unspecified"),
                    default=entry.get("default", False),
                    notes=entry.get("notes"),
                )
                for entry in data.get("models", [])
            ]

        # Fallback catalogue if YAML or file is unavailable
        return [
            ModelInfo(
                name="seneca-cybersecurity-q4",
                role="malware-analysis",
                size="~4.5 GB",
                source="ollama",
                default=True,
                notes="Default security model for quickstarts",
            ),
            ModelInfo(
                name="whiterabbitneo-7b",
                role="red-team",
                size="~4.5 GB",
                source="ollama",
                notes="Offensive testing and exploitation",
            ),
        ]

    def default_model(self) -> ModelInfo:
        for model in self.models:
            if model.default:
                return model
        return self.models[0]

    def list_models(self) -> List[ModelInfo]:
        return self.models

    def as_dict(self) -> List[Dict[str, str]]:
        return [
            {
                "name": model.name,
                "role": model.role,
                "size": model.size,
                "source": model.source,
                "default": str(model.default),
                "notes": model.notes or "",
            }
            for model in self.models
        ]
