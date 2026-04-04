---
title: Releasing a new version
icon: lucide/rocket
---

# Releasing a new version

Release version numbers should follow [Semantic Versioning][semver].

To create a new release, simply create and push a tag with the new release
version number:

```sh
git tag vX.Y.Z  # for example, v1.2.3
git push --tags
```

* A corresponding [GitHub release][github-releases]
  will be created automatically.

    [![GitHub Release][github-release-badge]][github-release-latest]

* A release package will be built and [uploaded to PyPI][pypi-project].

    [![PyPI][pypi-badge]][pypi-project]

* A container image will be built and published to
  the [GitHub Container Registry (GHCR)][ghcr-project].

[ghcr-project]: https://github.com/smkent/copier-python/pkgs/container/copier-python
[github-release-latest]: https://github.com/smkent/copier-python/releases/latest
[github-releases]: https://github.com/smkent/copier-python/releases
[github-release-badge]: https://img.shields.io/github/v/release/smkent/copier-python
[pypi-badge]: https://img.shields.io/pypi/v/copier-python
[pypi-project]: https://pypi.org/project/copier-python/
