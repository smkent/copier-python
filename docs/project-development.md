---
title: Development workflow
icon: lucide/braces
---

# Project development workflow

## Cloning the repository

Run `poe setup` in new repository clones to enable git hooks:

```sh
git clone https://github.com/<github_user>/<project_name>
cd project_name
poe setup  # Enables git hooks
```

## Development tools

* `poe lint`: Run formatters and static checks
* `poe test`: Run tests

The `lint` and `test` tasks can also be run as a single combined command with:

```sh
poe lt
```

## Documentation server

Start the development server with:

```sh
poe docs
```

The documentation site will be served at:

[**http://localhost:8000**](http://localhost:8000){ .md-button .md-button--primary target="_blank" }

To use a different bind host/port, run `poe --help docs` for arguments info.
