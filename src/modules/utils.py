"""Lightweight utility helpers."""

from __future__ import annotations

from datetime import datetime
from typing import Any


def log(message: str, *, data: Any | None = None) -> None:
    """Print a timestamped log line; friendly for CLI demos and placeholders."""
    timestamp = datetime.utcnow().isoformat()
    suffix = f" | {data}" if data is not None else ""
    print(f"[{timestamp}] {message}{suffix}")
