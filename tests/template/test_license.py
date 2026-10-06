"""Snapshot tests for LICENSE template."""

from collections.abc import Callable
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from tests.utils import TEMPLATE_ROOT, license_choices


@pytest.mark.parametrize("copyright_license", license_choices.values())
def test_license(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    copyright_license: str,
) -> None:
    rendered = render_template(copyright_license=copyright_license)
    assert (rendered / "LICENSE").read_text() == snapshot


@pytest.mark.parametrize("copyright_license", license_choices.values())
def test_license_choices_have_templates(copyright_license: str) -> None:
    assert (
        TEMPLATE_ROOT / "includes" / "licenses" / copyright_license
    ).is_file()
