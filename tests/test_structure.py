"""Tests for rendered project file presence and absence."""

from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest


@pytest.mark.parametrize(
    ("extra_data", "expected_present", "expected_absent"),
    [
        pytest.param(
            {"enable_coverage": False, "enable_pypi": False},
            [
                "docs",
                "pyproject.toml",
                "zensical.toml",
                "README.md",
                "CONTRIBUTING.md",
                "CHANGELOG.md",
                "LICENSE",
                ".gitignore",
                ".pre-commit-config.yaml",
                "renovate.json",
                "MAINTAINING.md",
                ".github/workflows/ci.yaml",
                ".github/workflows/docs.yaml",
                ".github/workflows/audit.yaml",
            ],
            [
                "Dockerfile",
                ".dockerignore",
                "compose.yaml",
                ".github/workflows/release.yaml",
                ".github/workflows/container.yaml",
                ".github/workflows/ghcr.yaml",
            ],
            id="public_library_minimal",
        ),
        pytest.param(
            {"project_visibility": "private"},
            [],
            [".github", "MAINTAINING.md"],
            id="private",
        ),
        pytest.param(
            {"enable_pypi": True},
            [".github/workflows/release.yaml"],
            [],
            id="pypi",
        ),
        pytest.param(
            {"enable_container": True},
            [
                "Dockerfile",
                ".dockerignore",
                ".github/workflows/container.yaml",
                ".github/workflows/ghcr.yaml",
            ],
            ["compose.yaml"],
            id="container_library",
        ),
        pytest.param(
            {"enable_container": True, "project_type": "application"},
            ["Dockerfile", ".dockerignore", "compose.yaml"],
            [],
            id="container_application",
        ),
        pytest.param(
            {"enable_docs": True},
            ["docs", "zensical.toml", ".github/workflows/docs.yaml"],
            [],
            id="docs",
        ),
    ],
)
def test_structure(
    render_template: Callable[..., Path],
    extra_data: dict[str, Any],
    expected_present: list[str],
    expected_absent: list[str],
) -> None:
    rendered = render_template(**extra_data)
    for path in expected_present:
        assert (rendered / path).exists(), f"{path!r} should exist"
    for path in expected_absent:
        assert not (rendered / path).exists(), f"{path!r} should be absent"
