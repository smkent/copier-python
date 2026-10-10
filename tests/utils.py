from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, Self
from unittest.mock import MagicMock, patch

import yaml

if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Sequence

    import pytest


@dataclass
class DisallowCallable:
    request: pytest.FixtureRequest
    obj: object
    attr: str
    original: Callable[..., Any] = field(init=False)
    enabled: bool = field(default=False, init=False)
    mock_attr: MagicMock | None = field(default=None, init=False)

    @dataclass
    class DisallowedError(Exception):
        mock: DisallowCallable

        def __str__(self) -> str:
            fn = self.mock.original
            name = f"{fn.__module__}." + (
                getattr(fn, "__qualname__", None)
                or getattr(fn, "__name__", "(unknown)")
            )
            return f"`{name}` disallowed via {self.mock.request.fixturename}"

    def __post_init__(self) -> None:
        self.original = getattr(self.obj, self.attr)

    @contextmanager
    def __call__(self) -> Generator[Self]:

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if self.enabled:
                return self.original(*args, **kwargs)
            raise self.DisallowedError(self)

        with patch.object(
            self.obj, self.attr, autospec=True, side_effect=wrapper
        ) as mock_attr:
            self.mock_attr = mock_attr
            yield self

    @contextmanager
    def pause(self) -> Generator[None]:
        if self.mock_attr:
            with patch.object(self.obj, self.attr, self.original):
                yield
            self.mock_attr.assert_not_called()


@dataclass
class PythonVersionsSupported:
    minor_min: int
    minor_max: int

    @cached_property
    def minor_mid(self) -> int:
        return self.minor_min + round((self.minor_max - self.minor_min) / 2)

    @cached_property
    def min_param(self) -> Sequence[str]:
        return tuple(f"3.{v}" for v in (self.minor_min, self.minor_mid))

    @cached_property
    def min_param_full_range(self) -> Sequence[str]:
        return tuple(f"3.{v}" for v in (self.minor_min, self.minor_max))

    @cached_property
    def max_param(self) -> Sequence[str]:
        return (
            *(f"3.{v}" for v in (self.minor_mid, self.minor_max)),
            "No maximum",
        )


class Template:
    @cached_property
    def dir(self) -> Path:
        return Path(__file__).parent.parent

    @cached_property
    def config(self) -> dict[str, Any]:
        return yaml.safe_load((self.dir / "copier.yaml").read_text())

    @cached_property
    def choices(self) -> SimpleNamespace:
        return SimpleNamespace(
            **{
                k: list(choices.values())
                if isinstance(choices, dict)
                else choices
                for k, v in self.config.items()
                if isinstance(v, dict)
                and (choices := v.get("choices"))
                and isinstance(choices, (dict, list))
            }
        )

    @cached_property
    def python_versions(self) -> PythonVersionsSupported:
        python_versions_supported = self.config[
            "template_python_versions_supported"
        ]["default"]
        return PythonVersionsSupported(
            minor_min=int(python_versions_supported["min_minor"]),
            minor_max=int(python_versions_supported["max_minor"]),
        )


template = Template()
