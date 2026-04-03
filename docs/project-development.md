---
icon: lucide/braces
---

# Project development workflow

## Cloning the repository

Run `poe setup` in new repository clones to enable git hooks:

```sh
git clone https://github.com/<github_user>/<project_name>
cd project_name
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

## Creating a release

Create and push a tag:

```sh
git tag vX.Y.Z
git push --tags
```
