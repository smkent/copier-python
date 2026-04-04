---
title: Releasing a project
icon: lucide/rocket
---

# Releasing a project

Release version numbers should follow [Semantic Versioning][semver].

To create a new release, simply create and push a tag with the new release
version number:

```sh
git tag vX.Y.Z  # for example, v1.2.3
git push --tags
```

* A corresponding GitHub release will be created automatically.
* If PyPI publishing is enabled, a release package will be built and uploaded to
  PyPI.
* If container image build and publishing is enabled, a container image will be
  built and published to the [GitHub Container Registry (GHCR)][ghcr-docs].

[ghcr-docs]: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
[semver]: https://semver.org/
