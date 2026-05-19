"""Snapshot tests for AGENTS.md template."""

from collections.abc import Callable
from pathlib import Path

from syrupy.assertion import SnapshotAssertion


def test_agents(
    render_template: Callable[..., Path], snapshot: SnapshotAssertion
) -> None:
    rendered = render_template()
    assert (rendered / "AGENTS.md").read_text() == snapshot
