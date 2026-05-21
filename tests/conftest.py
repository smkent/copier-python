from __future__ import annotations

import subprocess
import warnings
from pathlib import Path
from typing import TYPE_CHECKING, Any

import copier
import pytest

from copier_python.__main__ import setup_env

from .utils import DisallowCallable

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

TEMPLATE_ROOT = Path(__file__).parent.parent

DEFAULT_DATA: dict[str, Any] = {
    "project_name": "PKFire",
    "project_description": "Onett Little League",
    "project_type": "library",
    "project_visibility": "public",
    "python_version_minimum": "3.10",
    "user_name": "Ness",
    "user_email": "ness@onett.example.com",
    "github_user": "ness",
    "copyright_holder": "Ness",
    "copyright_holder_email": "ness@onett.example.com",
    "copyright_year": "1995",
    "copyright_license": "MIT",
}


@pytest.fixture(scope="session", autouse=True)
def ensure_env() -> None:
    setup_env()


@pytest.fixture(autouse=True)
def disallow_subprocess(
    request: pytest.FixtureRequest,
) -> Iterator[DisallowCallable]:
    with DisallowCallable(request, subprocess.Popen, "__init__")() as mock:
        yield mock


@pytest.fixture
def allow_subprocess(disallow_subprocess: DisallowCallable) -> Iterator[None]:
    with disallow_subprocess.pause():
        yield


@pytest.fixture
def render_template(
    tmp_path: Path, disallow_subprocess: DisallowCallable
) -> Callable[..., Path]:
    def _render(*, vcs_ref: str = "HEAD", **kwargs: Any) -> Path:
        worktree = tmp_path / "project"
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                category=copier.errors.DirtyLocalWarning,
            )
            with disallow_subprocess.pause():
                copier.run_copy(
                    src_path=str(TEMPLATE_ROOT),
                    dst_path=str(worktree),
                    data={**DEFAULT_DATA, **(kwargs or {})},
                    vcs_ref=vcs_ref,
                    defaults=True,
                    overwrite=True,
                    unsafe=False,
                )
        return worktree

    return _render
