"""Configuration helpers for converter runtime."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ConverterConfig:
    """Runtime configuration loaded from args/env."""

    database_url: str
    batch_size: int = 500


def get_default_database_url() -> str:
    """Return default DB URL with SQLite fallback."""
    return os.getenv("DATABASE_URL", "sqlite:///converter/pragmatic_bim.db")
