"""Snapshot tests for LICENSE template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from tests.utils import license_choices


@pytest.mark.parametrize("copyright_license", license_choices.values())
def test_license(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    copyright_license: str,
) -> None:
    rendered = render_template(copyright_license=copyright_license)
    assert (rendered / "LICENSE").read_text() == snapshot
