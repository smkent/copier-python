from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import template

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


@pytest.mark.parametrize(
    ("project_visibility", "config_path"),
    [
        ("public", ".github/commit-check.toml"),
        ("private", "commit-check.toml"),
    ],
)
def test_commit_check_config(
    render_template: Callable[..., Path],
    project_visibility: str,
    config_path: str,
) -> None:
    rendered = render_template(project_visibility=project_visibility)
    assert (rendered / config_path).read_text() == (
        template.dir / "includes" / "commit-check.toml"
    ).read_text()
