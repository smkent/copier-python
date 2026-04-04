"""Snapshot tests for zensical.toml template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
def test_docs_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_pypi: bool,
) -> None:
    rendered = render_template(
        project_visibility="public",
        enable_pypi=enable_pypi,
        enable_docs=True,
    )
    for doc_file in ["setup.md", "releasing.md"]:
        assert (rendered / "docs" / doc_file).read_text() == snapshot


@pytest.mark.parametrize("project_visibility", ["public", "private"])
@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
def test_docs_development_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    project_visibility: str,
    enable_pypi: bool,
) -> None:
    rendered = render_template(
        project_visibility=project_visibility,
        enable_pypi=enable_pypi,
        enable_docs=True,
    )
    for doc_file in ["requirements.md", "workflow.md", "updates.md"]:
        assert (
            rendered / "docs" / "development" / doc_file
        ).read_text() == snapshot
