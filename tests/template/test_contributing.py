"""Snapshot tests for CONTRIBUTING.md template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from tests.utils import license_choices


@pytest.mark.parametrize(
    "enable_docs",
    [pytest.param(True, id="docs"), pytest.param(False, id="no_docs")],
)
def test_contributing_features(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    *,
    enable_docs: bool,
) -> None:
    rendered = render_template(enable_docs=enable_docs)
    assert (rendered / "CONTRIBUTING.md").read_text() == snapshot


@pytest.mark.parametrize("copyright_license", license_choices.values())
def test_contributing_license(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    copyright_license: str,
) -> None:
    rendered = render_template(copyright_license=copyright_license)
    assert (rendered / "CONTRIBUTING.md").read_text() == snapshot
