# Contributing to copier-python

## Development setup

### Prerequisites

- [Astral's **uv** Python project manager][uv]
- [`poethepoet`][poe] task runner: `uv tool install poethepoet`

### Project setup

```sh
git clone https://github.com/smkent/copier-python
cd copier-python
uv sync
uv run poe setup  # Enables pre-commit hooks
```

## Common tasks

| Command | Description |
|---|---|
| `poe docs` | Run documentation server locally |
| `poe lint` | Run all formatters and static checks |
| `poe lt` | Run all formatters, static checks and tests (`lint` and `test`) |
| `poe snapup` | Update test snapshots |
| `poe test` | Run tests |

[poe]: https://poethepoet.naln1.net/
[uv]: https://docs.astral.sh/uv/
