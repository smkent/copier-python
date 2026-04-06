"""Snapshot tests for Dockerfile templates."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize("python_version_minimum", ["3.10", "3.12"])
@pytest.mark.parametrize(
    "python_version_maximum", ["3.12", "3.14", "No maximum"]
)
def test_workflows_container(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    python_version_minimum: str,
    python_version_maximum: str,
) -> None:
    rendered = render_template(
        project_visibility="public",
        enable_container=True,
        python_version_minimum=python_version_minimum,
        python_version_maximum=python_version_maximum,
    )
    assert (rendered / "Dockerfile").read_text() == snapshot
