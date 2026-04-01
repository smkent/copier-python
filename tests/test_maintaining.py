"""Snapshot tests for MAINTAINING.md template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "enable_pypi",
    [pytest.param(True, id="pypi"), pytest.param(False, id="no_pypi")],
)
@pytest.mark.parametrize(
    "enable_container",
    [
        pytest.param(True, id="container"),
        pytest.param(False, id="no_container"),
    ],
)
@pytest.mark.parametrize(
    "enable_docs",
    [pytest.param(True, id="docs"), pytest.param(False, id="no_docs")],
)
def test_maintaining_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_pypi: bool,
    enable_docs: bool,
    enable_container: bool,
) -> None:
    rendered = render_template(
        enable_pypi=enable_pypi,
        enable_docs=enable_docs,
        enable_container=enable_container,
    )
    assert (rendered / "MAINTAINING.md").read_text() == snapshot
