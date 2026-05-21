"""Snapshot tests for README.md template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "enable_coverage",
    [pytest.param(True, id="coverage"), pytest.param(False, id="no_coverage")],
)
@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
@pytest.mark.parametrize(
    "template_attribution",
    [
        pytest.param(True, id="attribution"),
        pytest.param(False, id="no_attribution"),
    ],
)
def test_readme_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_coverage: bool,
    enable_pypi: bool,
    template_attribution: bool,
) -> None:
    rendered = render_template(
        enable_coverage=enable_coverage,
        enable_pypi=enable_pypi,
        template_attribution=template_attribution,
    )
    assert (rendered / "README.md").read_text() == snapshot


@pytest.mark.parametrize("project_visibility", ["public", "private"])
def test_readme_project_visibility(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    project_visibility: str,
) -> None:
    rendered = render_template(project_visibility=project_visibility)
    assert (rendered / "README.md").read_text() == snapshot


@pytest.mark.parametrize("project_type", ["application", "library"])
def test_readme_project_type(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    project_type: str,
) -> None:
    rendered = render_template(project_type=project_type)
    assert (rendered / "README.md").read_text() == snapshot
