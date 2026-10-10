"""Snapshot tests for LICENSE template."""

from collections.abc import Callable
from pathlib import Path

import pytest
import yaml
from syrupy.assertion import SnapshotAssertion

from tests.utils import TEMPLATE_ROOT, choices


@pytest.mark.parametrize("copyright_license", choices["copyright_license"])
def test_license(
    render_template: Callable[..., Path],
    snapshot: SnapshotAssertion,
    copyright_license: str,
) -> None:
    rendered = render_template(copyright_license=copyright_license)
    for name in ["LICENSE", "COPYING.LESSER", "COPYING"]:
        if (rendered / name).exists():
            assert (rendered / name).read_text() == snapshot


@pytest.mark.parametrize("copyright_license", choices["copyright_license"])
def test_license_files(
    render_template: Callable[..., Path], copyright_license: str
) -> None:
    if copyright_license.startswith("LGPL-"):
        expected = ["COPYING", "COPYING.LESSER"]
    elif "GPL-" in copyright_license:
        expected = ["COPYING"]
    else:
        expected = ["LICENSE"]
    rendered = render_template(copyright_license=copyright_license)
    assert (
        sorted(
            p.name
            for p in rendered.iterdir()
            if p.name in {"LICENSE", "COPYING", "COPYING.LESSER"}
        )
        == expected
    )


@pytest.mark.parametrize("project_type", ["application", "library"])
def test_license_default(
    render_template: Callable[..., Path], project_type: str
) -> None:
    rendered = render_template(
        copyright_license=None, project_type=project_type
    )
    answers = yaml.safe_load((rendered / ".copier-answers.yml").read_text())
    assert answers["copyright_license"] == (
        "LGPL-3.0-only" if project_type == "library" else "GPL-3.0-only"
    )


@pytest.mark.parametrize("copyright_license", choices["copyright_license"])
def test_license_choices_have_templates(copyright_license: str) -> None:
    assert (
        TEMPLATE_ROOT / "includes" / "licenses" / copyright_license
    ).is_file()


@pytest.mark.parametrize(
    ("previous_license", "expected_license"),
    [
        ("AGPL-3.0", "AGPL-3.0-only"),
        ("GPL-3.0", "GPL-3.0-only"),
        ("LGPL-3.0", "LGPL-3.0-only"),
        ("GPL-3.0-or-later", "GPL-3.0-or-later"),
        ("MIT", "MIT"),
    ],
)
def test_license_previous_answer(
    render_template: Callable[..., Path],
    previous_license: str,
    expected_license: str,
) -> None:
    rendered = render_template(
        copyright_license=None,
        previous_answers={
            "copyright_license": previous_license,
            "template_attribution": False,
        },
    )
    answers = yaml.safe_load((rendered / ".copier-answers.yml").read_text())
    assert answers["copyright_license"] == expected_license
    assert (
        f'license = "{expected_license}"'
        in (rendered / "pyproject.toml").read_text()
    )
