"""Snapshot tests for AGENTS.md template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from tests.utils import template


@pytest.mark.parametrize(
    "llm_contribution_policy", template.choices.llm_contribution_policy
)
def test_agents(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    llm_contribution_policy: str,
) -> None:
    rendered = render_template(llm_contribution_policy=llm_contribution_policy)
    assert (rendered / "AGENTS.md").read_text() == snapshot
