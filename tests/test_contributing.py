"""Snapshot tests for CONTRIBUTING.md template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "enable_docs",
    [pytest.param(True, id="docs"), pytest.param(False, id="no_docs")],
)
def test_maintaining_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_docs: bool,
) -> None:
    rendered = render_template(enable_docs=enable_docs)
    assert (rendered / "CONTRIBUTING.md").read_text() == snapshot
