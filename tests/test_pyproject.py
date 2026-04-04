"""Snapshot tests for pyproject.toml template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize("project_visibility", ["public", "private"])
@pytest.mark.parametrize("python_version_minimum", ["3.10", "3.14"])
@pytest.mark.parametrize(
    "enable_docs",
    [pytest.param(True, id="docs"), pytest.param(False, id="no_docs")],
)
def test_maintaining_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    project_visibility: bool,
    python_version_minimum: str,
    enable_docs: bool,
) -> None:
    rendered = render_template(
        project_visibility=project_visibility,
        python_version_minimum=python_version_minimum,
        enable_docs=enable_docs,
    )
    assert (rendered / "pyproject.toml").read_text() == snapshot
