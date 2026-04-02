"""Snapshot tests for zensical.toml template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize("project_visibility", ["public", "private"])
@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
def test_zensical_features(
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
    assert (rendered / "zensical.toml").read_text() == snapshot
