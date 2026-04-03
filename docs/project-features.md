---
icon: lucide/settings
---

# Preparing project features

!!! tip
    These instructions are also present in your new project, with links directly
    to your project's specific settings pages! To view these instructions in
    your project:

    1. Start the local documentation server: `poe docs`
    2. In your browser:

        1. Open **<http://localhost:8000>**
        2. Click the **Development** tab
        3. Click **Maintaining** in the left nav bar


## GitHub repository

[Repository Settings → General][github-settings-docs]:

- [x] Allow merge commits
- [ ] Allow squash merging
- [ ] Allow rebase merging
- [x] Automatically delete head branches

Repository Settings → Branches → Add branch protection rule for the default branch
(`main`):

- [x] Restrict deletions
- [x] Require a pull request before merging
- [x] Block force pushes

## Renovate

Ensure the [Renovate app][renovate] is installed on your account, then enable
it for your repository.

## PyPI publishing

!!! info "Only needed if your project will publish packages to PyPI"

This template uses [trusted publishing][pypi-trusted-publishing] so no API
tokens need to be stored as secrets.

1. On PyPI, add a (pending) trusted publisher in your
   [Trusted Publisher Management][pypi-publishing-settings] settings:
     - Publisher: GitHub Actions
     - Owner: `<your-github-user>`
     - Repository: `<your-project-name>`
     - Workflow: `release.yaml`
     - Environment: `pypi`
2. Create the `pypi` environment in the GitHub repository:
   Repository Settings → Environments → New environment → `pypi`
3. Publish a release by pushing a tag:
   ```sh
   git tag v0.1.0  # or your desired first version number
   git push --tags
   ```

## Container registry (ghcr.io)

!!! info "Only needed if your project will build and publish container images"

Enable write access for Actions:

Repository Settings → Actions → General → Workflow permissions
→ Read and write permissions

## GitHub Pages

!!! info "Only needed if your project will publish the documentation site"

Repository Settings → Pages → Source → GitHub Actions

[copier]: https://copier.readthedocs.io
[github-new]: https://github.com/new
[github-settings-docs]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features
[pypi-publishing-settings]: https://pypi.org/manage/account/publishing/
[pypi-trusted-publishing]: https://docs.pypi.org/trusted-publishers/
[pypi]: https://pypi.org
[pypi-login]: https://pypi.org/account/login/
[pyproject-name]: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#name
[renovate]: https://github.com/apps/renovate
[uv]: https://docs.astral.sh/uv/
