---
title: Development workflow
icon: lucide/braces
---

# Project development workflow

## Cloning the repository

Run `poe setup` in new repository clones to enable git hooks:

```sh
git clone https://github.com/smkent/copier-python
cd copier-python
poe setup  # Enables git hooks
```

## Development tools

* `poe lint`: Run formatters and static checks
* `poe test`: Run tests

The `lint` and `test` tasks can also be run as a single combined command with:

```sh
poe lt
```

### Test snapshots

Many copier-python tests compare template-rendered files with saved snapshots.
When templates are modified, the snapshots need to be updated. Update test
snapshots by running:

```sh
poe snapup
```

## Documentation server

Start the development server with:

```sh
poe docs
```

The documentation site will be served at **<http://localhost:8000>**.

To use a different bind host/port, run `poe --help docs` for arguments info.
