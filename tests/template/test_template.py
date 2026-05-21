"""Tests for the copier-python template."""

import subprocess
from collections.abc import Callable
from pathlib import Path

import pytest


@pytest.mark.usefixtures("allow_subprocess")
def test_template_render_lint_test(
    render_template: Callable[..., Path],
) -> None:
    rendered = render_template(
        project_visibility="public",
        enable_container=True,
        enable_coverage=True,
        enable_docs=True,
        enable_pypi=True,
    )
    subprocess.run(["uv", "run", "poe", "init"], cwd=rendered, check=True)
    subprocess.run(["uv", "run", "poe", "lt"], cwd=rendered, check=True)
