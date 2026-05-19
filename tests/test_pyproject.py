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
@pytest.mark.parametrize(
    "enable_syrupy",
    [pytest.param(True, id="syrupy"), pytest.param(False, id="no_syrupy")],
)
@pytest.mark.parametrize(
    "enable_xdist",
    [pytest.param(True, id="xdist"), pytest.param(False, id="no_xdist")],
)
def test_pyproject_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    project_visibility: bool,
    python_version_minimum: str,
    enable_docs: bool,
    enable_syrupy: bool,
    enable_xdist: bool,
) -> None:
    rendered = render_template(
        project_visibility=project_visibility,
        python_version_minimum=python_version_minimum,
        enable_docs=enable_docs,
        enable_features=[
            *(["syrupy"] if enable_syrupy else []),
            *(["xdist"] if enable_xdist else []),
        ],
    )
    assert (rendered / "pyproject.toml").read_text() == snapshot


@pytest.mark.parametrize("python_version_minimum", ["3.10", "3.12"])
@pytest.mark.parametrize(
    "python_version_maximum", ["3.12", "3.14", "No maximum"]
)
def test_pyproject_versions(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    python_version_minimum: str,
    python_version_maximum: str,
) -> None:
    rendered = render_template(
        python_version_minimum=python_version_minimum,
        python_version_maximum=python_version_maximum,
    )
    assert (rendered / "pyproject.toml").read_text() == snapshot
