"""Snapshot tests for LICENSE template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion


@pytest.mark.parametrize(
    "copyright_license",
    [
        "AGPL-3.0",
        "Apache-2.0",
        "BSD-3-Clause",
        "CC-BY-4.0",
        "CC-BY-SA-4.0",
        "CC0-1.0",
        "GPL-3.0",
        "ISC",
        "LGPL-3.0",
        "MIT",
    ],
)
def test_license(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    copyright_license: str,
) -> None:
    rendered = render_template(copyright_license=copyright_license)
    assert (rendered / "README.md").read_text() == snapshot
