---
title: Development workflow
icon: lucide/braces
---

# copier-python development workflow

## Cloning the repository

Run `poe setup` in new repository clones to enable git hooks:

```sh
git clone https://github.com/smkent/copier-python
cd copier-python
poe setup  # Enables git hooks
```

## Local template usage

While making development changes to copier-python, the local template can be
used to create projects. To do so, run `copier copy` with the `-r`/`--vcs-ref`
argument:

```sh
copier copy -r HEAD path/to/copier-python/clone/ path/to/new/project/
```

This will render the new project from the current template state including
uncommitted changes.

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

The documentation site will be served at:

[**http://localhost:8000**](http://localhost:8000){ .md-button .md-button--primary target="_blank" }

To use a different bind host/port, run `poe --help docs` for arguments info.
