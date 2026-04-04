"""Snapshot tests for GitHub workflow templates."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "enable_coverage",
    [pytest.param(True, id="coverage"), pytest.param(False, id="no_coverage")],
)
@pytest.mark.parametrize(
    "enable_docs",
    [pytest.param(True, id="docs"), pytest.param(False, id="no_docs")],
)
def test_workflows_ci(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_coverage: bool,
    enable_docs: bool,
) -> None:
    rendered = render_template(
        project_type="application",
        project_visibility="public",
        enable_coverage=enable_coverage,
        enable_docs=enable_docs,
    )
    assert (
        rendered / ".github" / "workflows" / "ci.yaml"
    ).read_text() == snapshot


@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
def test_workflows_release(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_pypi: bool,
) -> None:
    rendered = render_template(
        project_type="application",
        project_visibility="public",
        enable_pypi=enable_pypi,
    )
    assert (
        rendered / ".github" / "workflows" / "release.yaml"
    ).read_text() == snapshot
