"""Snapshot tests for Dockerfile templates."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from tests.utils import template


@pytest.mark.parametrize(
    "python_version_minimum", template.python_versions.min_param
)
@pytest.mark.parametrize(
    "python_version_maximum", template.python_versions.max_param
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
