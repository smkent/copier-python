"""Shared test fixtures."""

import warnings
from collections.abc import Callable
from pathlib import Path
from typing import Any

import copier
import pytest

TEMPLATE_ROOT = Path(__file__).parent.parent

DEFAULT_DATA: dict[str, Any] = {
    "project_name": "PKFire",
    "project_description": "Onett Little League",
    "project_type": "library",
    "project_visibility": "public",
    "python_version_minimum": "3.10",
    "user_name": "Ness",
    "user_email": "ness@onett.example.com",
    "github_user": "ness",
    "copyright_holder": "Ness",
    "copyright_holder_email": "ness@onett.example.com",
    "copyright_year": "1995",
    "copyright_license": "MIT",
}


@pytest.fixture
def render_template(tmp_path: Path) -> Callable[..., Path]:
    def _render(**kwargs: Any) -> Path:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=copier.errors.DirtyLocalWarning,
            )
            copier.run_copy(
                src_path=str(TEMPLATE_ROOT),
                dst_path=str(tmp_path),
                data={**DEFAULT_DATA, **(kwargs or {})},
                vcs_ref="HEAD",
                defaults=True,
                overwrite=True,
                unsafe=False,
            )
        return tmp_path

    return _render
