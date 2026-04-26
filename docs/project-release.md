---
title: Releasing a project
icon: lucide/rocket
---

# Releasing a project

Release version numbers should follow [Semantic Versioning][semver].

To create a release, run `poe release` with one of `patch`, `minor`, or `major`
corresponding to the version number component to update:

```sh
poe release patch|minor|major
```

A new tag with the new release version number will be created automatically
using [bump-my-version][bump-my-version] (for example, `v1.2.3`).

Afterward, push the new release tag:

```sh
git push --tags
```

* A corresponding GitHub release will be created automatically.
* If PyPI publishing is enabled, a release package will be built and uploaded to
  PyPI.
* If container image build and publishing is enabled, a container image will be
  built and published to the [GitHub Container Registry (GHCR)][ghcr-docs].

[bump-my-version]: https://callowayproject.github.io/bump-my-version/
[ghcr-docs]: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
[semver]: https://semver.org/
