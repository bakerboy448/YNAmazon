# CHANGELOG


## v0.9.0 (2026-03-13)

### Build System

- **deps**: Bump pillow from 9.5.0 to 11.3.0 ([#1](https://github.com/bakerboy448/YNAmazon/pull/1),
  [`d0b3a9b`](https://github.com/bakerboy448/YNAmazon/commit/d0b3a9b99d9816127d981c165189f438f2ade795))

Bumps [pillow](https://github.com/python-pillow/Pillow) from 9.5.0 to 11.3.0. <details>
  <summary>Release notes</summary> <p><em>Sourced from <a
  href="https://github.com/python-pillow/Pillow/releases">pillow's releases</a>.</em></p>
  <blockquote> <h2>11.3.0</h2> <p><a
  href="https://pillow.readthedocs.io/en/stable/releasenotes/11.3.0.html">https://pillow.readthedocs.io/en/stable/releasenotes/11.3.0.html</a></p>
  <h2>Deprecations</h2> <ul> <li>Deprecate fromarray mode argument <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9018">#9018</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Deprecate saving I mode
  images as PNG <a href="https://redirect.github.com/python-pillow/Pillow/issues/9023">#9023</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> </ul>
  <h2>Documentation</h2> <ul> <li>Added release notes for <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9041">#9041</a> <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9042">#9042</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Add release notes for
  <a href="https://redirect.github.com/python-pillow/Pillow/issues/8912">#8912</a> and <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8969">#8969</a> <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9019">#9019</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>ImageFont does not
  handle multiline text <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9000">#9000</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Updated Ubuntu CI
  targets <a href="https://redirect.github.com/python-pillow/Pillow/issues/8988">#8988</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update MinGW package
  names <a href="https://redirect.github.com/python-pillow/Pillow/issues/8987">#8987</a> [<a
  href="https://github.com/H4M5TER"><code>@​H4M5TER</code></a>]</li> <li>Updated docstring <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8943">#8943</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Mention that tobytes()
  with the raw encoder uses Pack.c <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8878">#8878</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Refactor docs
  <code>Makefile</code> <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8933">#8933</a> [<a
  href="https://github.com/hugovk"><code>@​hugovk</code></a>]</li> <li>Add template for quarterly
  release issue <a href="https://redirect.github.com/python-pillow/Pillow/issues/8932">#8932</a> [<a
  href="https://github.com/aclark4life"><code>@​aclark4life</code></a>]</li> <li>Add list of third
  party plugins <a href="https://redirect.github.com/python-pillow/Pillow/issues/8910">#8910</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update redirected URL
  <a href="https://redirect.github.com/python-pillow/Pillow/issues/8919">#8919</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Docs: use sentence case
  for headers <a href="https://redirect.github.com/python-pillow/Pillow/issues/8914">#8914</a> [<a
  href="https://github.com/hugovk"><code>@​hugovk</code></a>]</li> <li>Docs: remove unused Makefile
  targets <a href="https://redirect.github.com/python-pillow/Pillow/issues/8917">#8917</a> [<a
  href="https://github.com/hugovk"><code>@​hugovk</code></a>]</li> <li>Remove indentation from lists
  <a href="https://redirect.github.com/python-pillow/Pillow/issues/8915">#8915</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Python 3.13 is tested
  on Arch <a href="https://redirect.github.com/python-pillow/Pillow/issues/8894">#8894</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Move XV Thumbnails to
  read only section <a href="https://redirect.github.com/python-pillow/Pillow/issues/8893">#8893</a>
  [<a href="https://github.com/aclark4life"><code>@​aclark4life</code></a>]</li> <li>Updated macOS
  tested Pillow versions <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8890">#8890</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> </ul> <h2>Dependencies</h2>
  <ul> <li>Add AVIF to wheels using only aomenc and dav1d AVIF codecs for reduced size <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8858">#8858</a> [<a
  href="https://github.com/fdintino"><code>@​fdintino</code></a>]</li> <li>Use same AVIF URL when
  fetching dependency <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8871">#8871</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update dependency mypy
  to v1.16.1 <a href="https://redirect.github.com/python-pillow/Pillow/issues/9026">#9026</a> [@<a
  href="https://github.com/apps/renovate">renovate[bot]</a>]</li> <li>Update libpng to 1.6.49 <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9014">#9014</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update dependency
  cibuildwheel to v3 <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9010">#9010</a> [@<a
  href="https://github.com/apps/renovate">renovate[bot]</a>]</li> <li>Updated libjpeg-turbo to 3.1.1
  <a href="https://redirect.github.com/python-pillow/Pillow/issues/9009">#9009</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update dependency mypy
  to v1.16.0 <a href="https://redirect.github.com/python-pillow/Pillow/issues/8991">#8991</a> [@<a
  href="https://github.com/apps/renovate">renovate[bot]</a>]</li> <li>Updated libpng to 1.6.48 <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8940">#8940</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Updated Ghostscript to
  10.5.1 <a href="https://redirect.github.com/python-pillow/Pillow/issues/8939">#8939</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Updated harfbuzz to
  11.2.1 <a href="https://redirect.github.com/python-pillow/Pillow/issues/8937">#8937</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Updated libavif to
  1.3.0 <a href="https://redirect.github.com/python-pillow/Pillow/issues/8949">#8949</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update dependency
  cibuildwheel to v2.23.3 <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8931">#8931</a> [@<a
  href="https://github.com/apps/renovate">renovate[bot]</a>]</li> <li>Updated harfbuzz to 11.1.0 <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8904">#8904</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> </ul> <h2>Testing</h2> <ul>
  <li>Add <code>match</code> parameter to <code>pytest.warns()</code> <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9038">#9038</a> [<a
  href="https://github.com/hugovk"><code>@​hugovk</code></a>]</li> <li>Increase pytest verbosity <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9040">#9040</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Improve SgiImagePlugin
  test coverage <a href="https://redirect.github.com/python-pillow/Pillow/issues/8896">#8896</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> <li>Update ruff pre-commit
  ID <a href="https://redirect.github.com/python-pillow/Pillow/issues/8994">#8994</a> [<a
  href="https://github.com/radarhere"><code>@​radarhere</code></a>]</li> </ul> <!-- raw HTML omitted
  --> </blockquote> <p>... (truncated)</p> </details> <details> <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst">pillow's
  changelog</a>.</em></p> <blockquote> <h1>Changelog (Pillow)</h1> <h2>11.1.0 and newer</h2> <p>See
  GitHub Releases:</p> <ul> <li><a
  href="https://github.com/python-pillow/Pillow/releases">https://github.com/python-pillow/Pillow/releases</a></li>
  </ul> <h2>11.0.0 (2024-10-15)</h2> <ul> <li> <p>Update licence to MIT-CMU <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8460">#8460</a> [hugovk]</p> </li>
  <li> <p>Conditionally define ImageCms type hint to avoid requiring core <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8197">#8197</a> [radarhere]</p>
  </li> <li> <p>Support writing LONG8 offsets in AppendingTiffWriter <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8417">#8417</a> [radarhere]</p>
  </li> <li> <p>Use ImageFile.MAXBLOCK when saving TIFF images <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8461">#8461</a> [radarhere]</p>
  </li> <li> <p>Do not close provided file handles with libtiff when saving <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8458">#8458</a> [radarhere]</p>
  </li> <li> <p>Support ImageFilter.BuiltinFilter for I;16* images <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8438">#8438</a> [radarhere]</p>
  </li> <li> <p>Use ImagingCore.ptr instead of ImagingCore.id <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8341">#8341</a> [homm, radarhere,
  hugovk]</p> </li> <li> <p>Updated EPS mode when opening images without transparency <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8281">#8281</a> [Yay295,
  radarhere]</p> </li> <li> <p>Use transparency when combining P frames from APNGs <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8443">#8443</a> [radarhere]</p>
  </li> <li> <p>Support all resampling filters when resizing I;16* images <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8422">#8422</a> [radarhere]</p>
  </li> <li> <p>Free memory on early return <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8413">#8413</a> [radarhere]</p>
  </li> <li> <p>Cast int before potentially exceeding INT_MAX <a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8402">#8402</a> [radarhere]</p>
  </li> </ul> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details> <details>
  <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python-pillow/Pillow/commit/89f1f4626a2aaf5f3d5ca6437f41def2998fbe09"><code>89f1f46</code></a>
  11.3.0 version bump</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/f2de251c769ed76acfe94b54cc87c2aee77bdadf"><code>f2de251</code></a>
  Updated check script paths (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9052">#9052</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/84855d11c8fd790d89507ac1c51a5e393178477a"><code>84855d1</code></a>
  Raise FileNotFoundError when opening an empty path (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9048">#9048</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/204d11d4da15879946c1120c43e6f75b2a338d5b"><code>204d11d</code></a>
  Raise FileNotFoundError when opening an empty path</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/2b39f7581e9637a7262c070d5cebb12fa70f2c86"><code>2b39f75</code></a>
  Handle IPTC TIFF tags with incorrect type (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8925">#8925</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/e7a53ba19b477cc30d35ef9e7aab4b79e5bba172"><code>e7a53ba</code></a>
  Do not update palette for L mode GIF frame (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8924">#8924</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/c22230b761254f3abf4af774d02b18b4b5eb6c71"><code>c22230b</code></a>
  Use save parameters as encoderinfo defaults (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9001">#9001</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/da10ed1cf3c4123a98a2f765d3beaf830d47d113"><code>da10ed1</code></a>
  Add support for iOS (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/9030">#9030</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/be2b4e78644fdc85e63f08a22514e4d32072439f"><code>be2b4e7</code></a>
  Fix qtables and quality scaling (<a
  href="https://redirect.github.com/python-pillow/Pillow/issues/8879">#8879</a>)</li> <li><a
  href="https://github.com/python-pillow/Pillow/commit/d4162f85056223098fef0ba3f87e58519ba2955f"><code>d4162f8</code></a>
  Updated return type</li> <li>Additional commits viewable in <a
  href="https://github.com/python-pillow/Pillow/compare/9.5.0...11.3.0">compare view</a></li> </ul>
  </details> <br />

[![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pillow&package-manager=uv&previous-version=9.5.0&new-version=11.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of
  the specified dependency - `@dependabot ignore this major version` will close this PR and stop
  Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it
  yourself) - `@dependabot ignore this minor version` will close this PR and stop Dependabot
  creating any more for this minor version (unless you reopen the PR or upgrade to it yourself) -
  `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for
  this dependency (unless you reopen the PR or upgrade to it yourself) You can disable automated
  security fix PRs for this repo from the [Security Alerts
  page](https://github.com/bakerboy448/YNAmazon/network/alerts).

</details>

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump the uv group across 1 directory with 5 updates
  ([#4](https://github.com/bakerboy448/YNAmazon/pull/4),
  [`7f89853`](https://github.com/bakerboy448/YNAmazon/commit/7f898534373b629ccd1d49cb105bc89cb2c8f7af))

Bumps the uv group with 5 updates in the / directory:

| Package | From | To | | --- | --- | --- | | [filelock](https://github.com/tox-dev/py-filelock) |
  `3.18.0` | `3.19.1` | | [h11](https://github.com/python-hyper/h11) | `0.14.0` | `0.16.0` | |
  [urllib3](https://github.com/urllib3/urllib3) | `2.3.0` | `2.6.3` | |
  [virtualenv](https://github.com/pypa/virtualenv) | `20.30.0` | `20.36.1` | |
  [setuptools](https://github.com/pypa/setuptools) | `78.1.0` | `78.1.1` |

Updates `filelock` from 3.18.0 to 3.19.1 <details> <summary>Release notes</summary> <p><em>Sourced
  from <a href="https://github.com/tox-dev/py-filelock/releases">filelock's releases</a>.</em></p>
  <blockquote> <h2>3.19.1</h2> <!-- raw HTML omitted --> <h2>What's Changed</h2> <ul> <li>add 3.14t
  (free threading) to matrix by <a href="https://github.com/paultiq"><code>@​paultiq</code></a> in
  <a href="https://redirect.github.com/tox-dev/filelock/pull/433">tox-dev/filelock#433</a></li>
  <li>Increase test coverage by <a href="https://github.com/paultiq"><code>@​paultiq</code></a> in
  <a href="https://redirect.github.com/tox-dev/filelock/pull/434">tox-dev/filelock#434</a></li>
  </ul> <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/paultiq"><code>@​paultiq</code></a> made their first contribution in <a
  href="https://redirect.github.com/tox-dev/filelock/pull/433">tox-dev/filelock#433</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/tox-dev/filelock/compare/3.19.0...3.19.1">https://github.com/tox-dev/filelock/compare/3.19.0...3.19.1</a></p>
  <h2>3.19.0</h2> <!-- raw HTML omitted --> <h2>What's Changed</h2> <ul> <li>Add support for 3.14 by
  <a href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/tox-dev/filelock/pull/432">tox-dev/filelock#432</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/tox-dev/filelock/compare/3.18.0...3.19.0">https://github.com/tox-dev/filelock/compare/3.18.0...3.19.0</a></p>
  </blockquote> </details> <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/tox-dev/filelock/blob/main/docs/changelog.rst">filelock's
  changelog</a>.</em></p> <blockquote> <p>########### Changelog ###########</p> <hr /> <p>3.25.2
  (2026-03-11)</p> <hr /> <ul> <li>🐛 fix(unix): suppress EIO on close in Docker bind mounts
  :pr:<code>513</code></li> </ul> <hr /> <p>3.25.1 (2026-03-09)</p> <hr /> <ul> <li>[pre-commit.ci]
  pre-commit autoupdate :pr:<code>510</code> - by :user:<code>pre-commit-ci[bot]</code></li> <li>🐛
  fix(win): restore best-effort lock file cleanup on release :pr:<code>511</code></li>
  <li>[pre-commit.ci] pre-commit autoupdate :pr:<code>508</code> - by
  :user:<code>pre-commit-ci[bot]</code></li> <li>📝 docs(logo): add branded project logo
  :pr:<code>507</code></li> </ul> <hr /> <p>3.25.0 (2026-03-01)</p> <hr /> <ul> <li>✨ feat(async):
  add AsyncReadWriteLock :pr:<code>506</code></li> <li>Standardize .github files to .yaml
  suffix</li> <li>build(deps): bump actions/download-artifact from 7 to 8 :pr:<code>503</code> - by
  :user:<code>dependabot[bot]</code></li> <li>build(deps): bump actions/upload-artifact from 6 to 7
  :pr:<code>502</code> - by :user:<code>dependabot[bot]</code></li> <li>Move SECURITY.md to
  .github/SECURITY.md</li> <li>Add security policy</li> <li>Add permissions to check workflow
  :pr:<code>500</code></li> <li>[pre-commit.ci] pre-commit autoupdate :pr:<code>499</code> - by
  :user:<code>pre-commit-ci[bot]</code></li> </ul> <hr /> <p>3.24.3 (2026-02-19)</p> <hr /> <ul>
  <li>🐛 fix(unix): handle ENOENT race on FUSE/NFS during acquire :pr:<code>495</code></li> <li>🐛
  fix(ci): add trailing blank line after changelog entries :pr:<code>492</code></li> </ul> <hr />
  <p>3.24.2 (2026-02-16)</p> <hr /> <ul> <li>🐛 fix(rw): close sqlite3 cursors and skip SoftFileLock
  Windows race :pr:<code>491</code></li> <li>🐛 fix(test): resolve flaky write non-starvation test
  :pr:<code>490</code></li> <li>📝 docs: restructure using Diataxis framework
  :pr:<code>489</code></li> </ul> <hr /> <p>3.24.1 (2026-02-15)</p> <hr /> <!-- raw HTML omitted -->
  </blockquote> <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/tox-dev/filelock/commit/8d1009f08a6a64624fad91d1079062ef31b8c2b4"><code>8d1009f</code></a>
  Update release.yaml</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/66a428e97a874b44b0310072f6c974226f55a472"><code>66a428e</code></a>
  Increase test coverage (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/434">#434</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/0dfc86eebd2c76ae959a409bcbc3112cc1ec5890"><code>0dfc86e</code></a>
  add 3.14 to matrix (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/433">#433</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/0c54837e318ebe8a692b529722430cb38134bf7c"><code>0c54837</code></a>
  Add support for 3.14 (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/432">#432</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/77d02f5ada3a1a92167b1beee35a7815cbde0fcf"><code>77d02f5</code></a>
  Bump actions/checkout from 4 to 5 (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/430">#430</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/bc972b33bf253bb9f08db32b19ffd4119a74706e"><code>bc972b3</code></a>
  [pre-commit.ci] pre-commit autoupdate (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/429">#429</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/78d02cb5ff42b22a56ad1a36755361a6b4601765"><code>78d02cb</code></a>
  Bump actions/download-artifact from 4 to 5 (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/428">#428</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/18cdb5d1c78a7a459463480303e9820f33cdf041"><code>18cdb5d</code></a>
  [pre-commit.ci] pre-commit autoupdate (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/427">#427</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/b198a096d2bae58596479497d18a82bbeec515c8"><code>b198a09</code></a>
  [pre-commit.ci] pre-commit autoupdate (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/426">#426</a>)</li> <li><a
  href="https://github.com/tox-dev/filelock/commit/6b097e76de603d9be6a24c5058b6fe53ef003afd"><code>6b097e7</code></a>
  [pre-commit.ci] pre-commit autoupdate (<a
  href="https://redirect.github.com/tox-dev/py-filelock/issues/425">#425</a>)</li> <li>Additional
  commits viewable in <a
  href="https://github.com/tox-dev/py-filelock/compare/3.18.0...3.19.1">compare view</a></li> </ul>
  </details> <br />

Updates `h11` from 0.14.0 to 0.16.0 <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/python-hyper/h11/commit/1c5b07581f058886c8bdd87adababd7d959dc7ca"><code>1c5b075</code></a>
  this time for surer</li> <li><a
  href="https://github.com/python-hyper/h11/commit/d9c369935e853a7ee1aeb7e481f6dddf9b9c9b8a"><code>d9c3699</code></a>
  this time for sure...</li> <li><a
  href="https://github.com/python-hyper/h11/commit/d91b9dd2290a25c8c3f5ec15feb57de5873e6e39"><code>d91b9dd</code></a>
  blacken</li> <li><a
  href="https://github.com/python-hyper/h11/commit/5a4683ca466b59bbab9b19cfea20ee157b31cee0"><code>5a4683c</code></a>
  Soothe mypy</li> <li><a
  href="https://github.com/python-hyper/h11/commit/9c9567f0a92d13a83a8d8ebdbc757c8c2d384536"><code>9c9567f</code></a>
  Bump version to 0.16.0</li> <li><a
  href="https://github.com/python-hyper/h11/commit/114803a29ce50116dc47951c690ad4892b1a36ed"><code>114803a</code></a>
  Merge commit from fork</li> <li><a
  href="https://github.com/python-hyper/h11/commit/9462006f6ce4941661888228cbd4ac1ea80689b0"><code>9462006</code></a>
  Bump version to 0.15.0</li> <li><a
  href="https://github.com/python-hyper/h11/commit/70a96bea8e55403e5d92db14c111432c6d7a8685"><code>70a96be</code></a>
  Merge pull request <a href="https://redirect.github.com/python-hyper/h11/issues/181">#181</a> from
  Julien00859/Julien00859/get_int_max_str_digits</li> <li><a
  href="https://github.com/python-hyper/h11/commit/60782ad107e538b9312aac7e1c119c8358bf797c"><code>60782ad</code></a>
  Reject Content-Length longer 1 billion TB</li> <li><a
  href="https://github.com/python-hyper/h11/commit/dff7cc397a26ed4acdedd92d1bda6c8f18a6ed9f"><code>dff7cc3</code></a>
  Validate Chunked-Encoding chunk footer</li> <li>Additional commits viewable in <a
  href="https://github.com/python-hyper/h11/compare/v0.14.0...v0.16.0">compare view</a></li> </ul>
  </details> <br />

Updates `urllib3` from 2.3.0 to 2.6.3 <details> <summary>Release notes</summary> <p><em>Sourced from
  <a href="https://github.com/urllib3/urllib3/releases">urllib3's releases</a>.</em></p>
  <blockquote> <h2>2.6.3</h2> <h2>🚀 urllib3 is fundraising for HTTP/2 support</h2> <p><a
  href="https://sethmlarson.dev/urllib3-is-fundraising-for-http2-support">urllib3 is raising
  ~$40,000 USD</a> to release HTTP/2 support and ensure long-term sustainable maintenance of the
  project after a sharp decline in financial support. If your company or organization uses Python
  and would benefit from HTTP/2 support in Requests, pip, cloud SDKs, and thousands of other
  projects <a href="https://opencollective.com/urllib3">please consider contributing financially</a>
  to ensure HTTP/2 support is developed sustainably and maintained for the long-haul.</p> <p>Thank
  you for your support.</p> <h2>Changes</h2> <ul> <li>Fixed a security issue where
  decompression-bomb safeguards of the streaming API were bypassed when HTTP redirects were
  followed. (CVE-2026-21441 reported by <a href="https://github.com/D47A"><code>@​D47A</code></a>,
  8.9 High, GHSA-38jv-5279-wg99)</li> <li>Started treating <code>Retry-After</code> times greater
  than 6 hours as 6 hours by default. (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3743">urllib3/urllib3#3743</a>)</li>
  <li>Fixed <code>urllib3.connection.VerifiedHTTPSConnection</code> on Emscripten. (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3752">urllib3/urllib3#3752</a>)</li>
  </ul> <h2>2.6.2</h2> <h2>🚀 urllib3 is fundraising for HTTP/2 support</h2> <p><a
  href="https://sethmlarson.dev/urllib3-is-fundraising-for-http2-support">urllib3 is raising
  ~$40,000 USD</a> to release HTTP/2 support and ensure long-term sustainable maintenance of the
  project after a sharp decline in financial support. If your company or organization uses Python
  and would benefit from HTTP/2 support in Requests, pip, cloud SDKs, and thousands of other
  projects <a href="https://opencollective.com/urllib3">please consider contributing financially</a>
  to ensure HTTP/2 support is developed sustainably and maintained for the long-haul.</p> <p>Thank
  you for your support.</p> <h2>Changes</h2> <ul> <li>Fixed <code>HTTPResponse.read_chunked()</code>
  to properly handle leftover data in the decoder's buffer when reading compressed chunked
  responses. (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3734">urllib3/urllib3#3734</a>)</li>
  </ul> <h2>2.6.1</h2> <h2>🚀 urllib3 is fundraising for HTTP/2 support</h2> <p><a
  href="https://sethmlarson.dev/urllib3-is-fundraising-for-http2-support">urllib3 is raising
  ~$40,000 USD</a> to release HTTP/2 support and ensure long-term sustainable maintenance of the
  project after a sharp decline in financial support. If your company or organization uses Python
  and would benefit from HTTP/2 support in Requests, pip, cloud SDKs, and thousands of other
  projects <a href="https://opencollective.com/urllib3">please consider contributing financially</a>
  to ensure HTTP/2 support is developed sustainably and maintained for the long-haul.</p> <p>Thank
  you for your support.</p> <h2>Changes</h2> <ul> <li>Restore previously removed
  <code>HTTPResponse.getheaders()</code> and <code>HTTPResponse.getheader()</code> methods. (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3731">#3731</a>)</li> </ul>
  <h2>2.6.0</h2> <h2>🚀 urllib3 is fundraising for HTTP/2 support</h2> <p><a
  href="https://sethmlarson.dev/urllib3-is-fundraising-for-http2-support">urllib3 is raising
  ~$40,000 USD</a> to release HTTP/2 support and ensure long-term sustainable maintenance of the
  project after a sharp decline in financial support. If your company or organization uses Python
  and would benefit from HTTP/2 support in Requests, pip, cloud SDKs, and thousands of other
  projects <a href="https://opencollective.com/urllib3">please consider contributing financially</a>
  to ensure HTTP/2 support is developed sustainably and maintained for the long-haul.</p> <p>Thank
  you for your support.</p> <h2>Security</h2> <ul> <li>Fixed a security issue where streaming API
  could improperly handle highly compressed HTTP content (&quot;decompression bombs&quot;) leading
  to excessive resource consumption even when a small amount of data was requested. Reading small
  chunks of compressed data is safer and much more efficient now. (CVE-2025-66471 reported by <a
  href="https://github.com/Cycloctane"><code>@​Cycloctane</code></a>, 8.9 High,
  GHSA-2xpw-w6gg-jr37)</li> <li>Fixed a security issue where an attacker could compose an HTTP
  response with virtually unlimited links in the <code>Content-Encoding</code> header, potentially
  leading to a denial of service (DoS) attack by exhausting system resources during decoding. The
  number of allowed chained encodings is now limited to 5. (CVE-2025-66418 reported by <a
  href="https://github.com/illia-v"><code>@​illia-v</code></a>, 8.9 High, GHSA-gm62-xv2j-4w53)</li>
  </ul> <blockquote> <p>[!IMPORTANT]</p> <ul> <li>If urllib3 is not installed with the optional
  <code>urllib3[brotli]</code> extra, but your environment contains a Brotli/brotlicffi/brotlipy
  package anyway, make sure to upgrade it to at least Brotli 1.2.0 or brotlicffi 1.2.0.0 to benefit
  from the security fixes and avoid warnings. Prefer using <code>urllib3[brotli]</code> to install a
  compatible Brotli package automatically.</li> </ul> </blockquote> <!-- raw HTML omitted -->
  </blockquote> <p>... (truncated)</p> </details> <details> <summary>Changelog</summary>
  <p><em>Sourced from <a href="https://github.com/urllib3/urllib3/blob/main/CHANGES.rst">urllib3's
  changelog</a>.</em></p> <blockquote> <h1>2.6.3 (2026-01-07)</h1> <ul> <li>Fixed a high-severity
  security issue where decompression-bomb safeguards of the streaming API were bypassed when HTTP
  redirects were followed. (<code>GHSA-38jv-5279-wg99
  &lt;https://github.com/urllib3/urllib3/security/advisories/GHSA-38jv-5279-wg99&gt;</code>__)</li>
  <li>Started treating <code>Retry-After</code> times greater than 6 hours as 6 hours by default.
  (<code>[#3743](https://github.com/urllib3/urllib3/issues/3743)
  &lt;https://github.com/urllib3/urllib3/issues/3743&gt;</code>__)</li> <li>Fixed
  <code>urllib3.connection.VerifiedHTTPSConnection</code> on Emscripten.
  (<code>[#3752](https://github.com/urllib3/urllib3/issues/3752)
  &lt;https://github.com/urllib3/urllib3/issues/3752&gt;</code>__)</li> </ul> <h1>2.6.2
  (2025-12-11)</h1> <ul> <li>Fixed <code>HTTPResponse.read_chunked()</code> to properly handle
  leftover data in the decoder's buffer when reading compressed chunked responses.
  (<code>[#3734](https://github.com/urllib3/urllib3/issues/3734)
  &lt;https://github.com/urllib3/urllib3/issues/3734&gt;</code>__)</li> </ul> <h1>2.6.1
  (2025-12-08)</h1> <ul> <li>Restore previously removed <code>HTTPResponse.getheaders()</code> and
  <code>HTTPResponse.getheader()</code> methods.
  (<code>[#3731](https://github.com/urllib3/urllib3/issues/3731)
  &lt;https://github.com/urllib3/urllib3/issues/3731&gt;</code>__)</li> </ul> <h1>2.6.0
  (2025-12-05)</h1> <h2>Security</h2> <ul> <li>Fixed a security issue where streaming API could
  improperly handle highly compressed HTTP content (&quot;decompression bombs&quot;) leading to
  excessive resource consumption even when a small amount of data was requested. Reading small
  chunks of compressed data is safer and much more efficient now. (<code>GHSA-2xpw-w6gg-jr37
  &lt;https://github.com/urllib3/urllib3/security/advisories/GHSA-2xpw-w6gg-jr37&gt;</code>__)</li>
  <li>Fixed a security issue where an attacker could compose an HTTP response with virtually
  unlimited links in the <code>Content-Encoding</code> header, potentially leading to a denial of
  service (DoS) attack by exhausting system resources during decoding. The number of allowed chained
  encodings is now limited to 5. (<code>GHSA-gm62-xv2j-4w53
  &lt;https://github.com/urllib3/urllib3/security/advisories/GHSA-gm62-xv2j-4w53&gt;</code>__)</li>
  </ul> <p>.. caution::</p> <ul> <li>If urllib3 is not installed with the optional
  <code>urllib3[brotli]</code> extra, but your environment contains a Brotli/brotlicffi/brotlipy
  package anyway, make sure to upgrade it to at least Brotli 1.2.0 or brotlicffi 1.2.0.0 to benefit
  from the security fixes and avoid warnings. Prefer using</li> </ul> <!-- raw HTML omitted -->
  </blockquote> <p>... (truncated)</p> </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/urllib3/urllib3/commit/0248277dd7ac0239204889ca991353ad3e3a1ddc"><code>0248277</code></a>
  Release 2.6.3</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/8864ac407bba8607950025e0979c4c69bc7abc7b"><code>8864ac4</code></a>
  Merge commit from fork</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/70cecb27ca99d56aaaeb63ac27ee270ef2b24c5c"><code>70cecb2</code></a>
  Fix Scorecard issues related to vulnerable dev dependencies (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3755">#3755</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/41f249abe1ef3e20768588969c4035aba060a359"><code>41f249a</code></a>
  Move &quot;v2.0 Migration Guide&quot; to the end of the table of contents (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3747">#3747</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/fd4dffd2fc544166b76151a2fa3d7b7c0eab540c"><code>fd4dffd</code></a>
  Patch <code>VerifiedHTTPSConnection</code> for Emscripten (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3752">#3752</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/13f0bfd55e4468fe1ea9c6f809d3a87b0f93ebab"><code>13f0bfd</code></a>
  Handle massive values in Retry-After when calculating time to sleep for (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3743">#3743</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/8c480bf87bcefd321b3a1ae47f04e908b6b2ed7b"><code>8c480bf</code></a>
  Bump actions/upload-artifact from 5.0.0 to 6.0.0 (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3748">#3748</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/4b40616e959c0a2c466e8075f2a785a9f99bb0c1"><code>4b40616</code></a>
  Bump actions/cache from 4.3.0 to 5.0.1 (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3750">#3750</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/82b8479663d037d220c883f1584dd01a43bb273b"><code>82b8479</code></a>
  Bump actions/download-artifact from 6.0.0 to 7.0.0 (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3749">#3749</a>)</li> <li><a
  href="https://github.com/urllib3/urllib3/commit/34284cb01700bb7d4fdd472f909e22393e9174e2"><code>34284cb</code></a>
  Mention experimental features in the security policy (<a
  href="https://redirect.github.com/urllib3/urllib3/issues/3746">#3746</a>)</li> <li>Additional
  commits viewable in <a href="https://github.com/urllib3/urllib3/compare/2.3.0...2.6.3">compare
  view</a></li> </ul> </details> <br />

Updates `virtualenv` from 20.30.0 to 20.36.1 <details> <summary>Release notes</summary>
  <p><em>Sourced from <a href="https://github.com/pypa/virtualenv/releases">virtualenv's
  releases</a>.</em></p> <blockquote> <h2>20.36.0</h2> <!-- raw HTML omitted --> <h2>What's
  Changed</h2> <ul> <li>release 20.35.3 by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2981">pypa/virtualenv#2981</a></li>
  <li>fix: Prevent NameError when accessing _DISTUTILS_PATCH during file ov… by <a
  href="https://github.com/gracetyy"><code>@​gracetyy</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2982">pypa/virtualenv#2982</a></li>
  <li>Upgrade pip and fix 3.15 picking old wheel by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2989">pypa/virtualenv#2989</a></li>
  <li>release 20.35.4 by <a href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in
  <a href="https://redirect.github.com/pypa/virtualenv/pull/2990">pypa/virtualenv#2990</a></li>
  <li>fix: wrong path on migrated venv by <a
  href="https://github.com/sk1234567891"><code>@​sk1234567891</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2996">pypa/virtualenv#2996</a></li>
  <li>test_too_many_open_files: assert on <code>errno.EMFILE</code> instead of <code>strerror</code>
  by <a href="https://github.com/pltrz"><code>@​pltrz</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3001">pypa/virtualenv#3001</a></li>
  <li>fix: update filelock dependency version to 3.20.1 to fix CVE CVE-2025-68146 by <a
  href="https://github.com/pythonhubdev"><code>@​pythonhubdev</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3002">pypa/virtualenv#3002</a></li>
  <li>fix: resolve EncodingWarning in tox upgrade environment by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3007">pypa/virtualenv#3007</a></li> <li>Fix
  Interpreter discovery bug wrt. Microsoft Store shortcut using Latin-1 by <a
  href="https://github.com/rahuldevikar"><code>@​rahuldevikar</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3006">pypa/virtualenv#3006</a></li> <li>Add
  support for PEP 440 version specifiers in the <code>--python</code> flag. by <a
  href="https://github.com/rahuldevikar"><code>@​rahuldevikar</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3008">pypa/virtualenv#3008</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/gracetyy"><code>@​gracetyy</code></a> made their first contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2982">pypa/virtualenv#2982</a></li> <li><a
  href="https://github.com/sk1234567891"><code>@​sk1234567891</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2996">pypa/virtualenv#2996</a></li> <li><a
  href="https://github.com/pltrz"><code>@​pltrz</code></a> made their first contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3001">pypa/virtualenv#3001</a></li> <li><a
  href="https://github.com/pythonhubdev"><code>@​pythonhubdev</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3002">pypa/virtualenv#3002</a></li> <li><a
  href="https://github.com/rahuldevikar"><code>@​rahuldevikar</code></a> made their first
  contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/3006">pypa/virtualenv#3006</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/pypa/virtualenv/compare/20.35.3...20.36.0">https://github.com/pypa/virtualenv/compare/20.35.3...20.36.0</a></p>
  <h2>20.35.4</h2> <!-- raw HTML omitted --> <h2>What's Changed</h2> <ul> <li>release 20.35.3 by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2981">pypa/virtualenv#2981</a></li>
  <li>fix: Prevent NameError when accessing _DISTUTILS_PATCH during file ov… by <a
  href="https://github.com/gracetyy"><code>@​gracetyy</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2982">pypa/virtualenv#2982</a></li>
  <li>Upgrade pip and fix 3.15 picking old wheel by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2989">pypa/virtualenv#2989</a></li> </ul>
  <h2>New Contributors</h2> <ul> <li><a
  href="https://github.com/gracetyy"><code>@​gracetyy</code></a> made their first contribution in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2982">pypa/virtualenv#2982</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/pypa/virtualenv/compare/20.35.3...20.35.4">https://github.com/pypa/virtualenv/compare/20.35.3...20.35.4</a></p>
  <h2>20.35.3</h2> <!-- raw HTML omitted --> <h2>What's Changed</h2> <ul> <li>release 20.35.1 by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2976">pypa/virtualenv#2976</a></li>
  <li>Revert out effort to extract discovery by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2978">pypa/virtualenv#2978</a></li>
  <li>release 20.35.2 by <a href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in
  <a href="https://redirect.github.com/pypa/virtualenv/pull/2980">pypa/virtualenv#2980</a></li>
  <li>test_too_many_open_files fails by <a
  href="https://github.com/gaborbernat"><code>@​gaborbernat</code></a> in <a
  href="https://redirect.github.com/pypa/virtualenv/pull/2979">pypa/virtualenv#2979</a></li> </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/pypa/virtualenv/compare/20.35.1...20.35.3">https://github.com/pypa/virtualenv/compare/20.35.1...20.35.3</a></p>
  <h2>20.35.2</h2> <!-- raw HTML omitted --> </blockquote> <p>... (truncated)</p> </details>
  <details> <summary>Changelog</summary> <p><em>Sourced from <a
  href="https://github.com/pypa/virtualenv/blob/main/docs/changelog.rst">virtualenv's
  changelog</a>.</em></p> <blockquote> <h1>Bugfixes - 20.36.1</h1> <ul> <li>Fix TOCTOU
  vulnerabilities in app_data and lock directory creation that could be exploited via symlink
  attacks - reported by :user:<code>tsigouris007</code>, fixed by :user:<code>gaborbernat</code>.
  (:issue:<code>3013</code>)</li> </ul> <hr /> <p>v20.36.0 (2026-01-07)</p> <hr /> <h1>Features -
  20.36.0</h1> <ul> <li>Add support for PEP 440 version specifiers in the <code>--python</code>
  flag. Users can now specify Python versions using operators like <code>&gt;=</code>,
  <code>&lt;=</code>, <code>~=</code>, etc. For example: <code>virtualenv
  --python=&quot;&gt;=3.12&quot; myenv</code> <code>. (:issue:</code>2994`)</li> </ul> <hr />
  <p>v20.35.4 (2025-10-28)</p> <hr /> <h1>Bugfixes - 20.35.4</h1> <ul> <li> <p>Fix race condition in
  <code>_virtualenv.py</code> when file is overwritten during import, preventing
  <code>NameError</code> when <code>_DISTUTILS_PATCH</code> is accessed - by
  :user:<code>gracetyy</code>. (:issue:<code>2969</code>)</p> </li> <li> <p>Upgrade embedded
  wheels:</p> <ul> <li>pip to <code>25.3</code> from <code>25.2</code>
  (:issue:<code>2989</code>)</li> </ul> </li> </ul> <hr /> <p>v20.35.3 (2025-10-10)</p> <hr />
  <h1>Bugfixes - 20.35.3</h1> <ul> <li>Accept RuntimeError in <code>test_too_many_open_files</code>,
  by :user:<code>esafak</code> (:issue:<code>2935</code>)</li> </ul> <hr /> <p>v20.35.2
  (2025-10-10)</p> <hr /> <h1>Bugfixes - 20.35.2</h1> <ul> <li>Revert out changes related to the
  extraction of the discovery module - by :user:<code>gaborbernat</code>.
  (:issue:<code>2978</code>)</li> </ul> <hr /> <p>v20.35.1 (2025-10-09)</p> <hr /> <!-- raw HTML
  omitted --> </blockquote> <p>... (truncated)</p> </details> <details> <summary>Commits</summary>
  <ul> <li><a
  href="https://github.com/pypa/virtualenv/commit/d0ad11d1146e81ea74d2461be9653f1da9cf3fd1"><code>d0ad11d</code></a>
  release 20.36.1</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/dec4cec5d16edaf83a00a658f32d1e032661cebc"><code>dec4cec</code></a>
  Merge pull request <a href="https://redirect.github.com/pypa/virtualenv/issues/3013">#3013</a>
  from gaborbernat/fix-sec</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/5fe5d38beb1273b489591a7b444f1018af2edf0a"><code>5fe5d38</code></a>
  release 20.36.0 (<a href="https://redirect.github.com/pypa/virtualenv/issues/3011">#3011</a>)</li>
  <li><a
  href="https://github.com/pypa/virtualenv/commit/9719376addaa710b61d9ed013774fa26f6224b4e"><code>9719376</code></a>
  release 20.36.0</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/0276db6fcf8849c519d75465f659b12aefb2acd8"><code>0276db6</code></a>
  Add support for PEP 440 version specifiers in the <code>--python</code> flag. (<a
  href="https://redirect.github.com/pypa/virtualenv/issues/3008">#3008</a>)</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/4f900c29044e17812981b5b98ddce45604858b7f"><code>4f900c2</code></a>
  Fix Interpreter discovery bug wrt. Microsoft Store shortcut using Latin-1 (<a
  href="https://redirect.github.com/pypa/virtualenv/issues/3">#3</a>...</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/13afcc62a3444d0386c8031d0a62277a8274ab07"><code>13afcc6</code></a>
  fix: resolve EncodingWarning in tox upgrade environment (<a

href="https://redirect.github.com/pypa/virtualenv/issues/3007">#3007</a>)</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/31b5d31581df3e3a7bbc55e52568b26dd01b0d57"><code>31b5d31</code></a>
  [pre-commit.ci] pre-commit autoupdate (<a
  href="https://redirect.github.com/pypa/virtualenv/issues/2997">#2997</a>)</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/7c284221b4751388801355fc6ebaa2abe60427bd"><code>7c28422</code></a>
  fix: update filelock dependency version to 3.20.1 to fix CVE CVE-2025-68146 (...</li> <li><a
  href="https://github.com/pypa/virtualenv/commit/365628c544cd5498fbf0a3b6c6a8c1f41d25a749"><code>365628c</code></a>
  test_too_many_open_files: assert on <code>errno.EMFILE</code> instead of <code>strerror</code> (<a
  href="https://redirect.github.com/pypa/virtualenv/issues/3001">#3001</a>)</li> <li>Additional
  commits viewable in <a href="https://github.com/pypa/virtualenv/compare/20.30.0...20.36.1">compare
  view</a></li> </ul> </details> <br />

Updates `setuptools` from 78.1.0 to 78.1.1 <details> <summary>Changelog</summary> <p><em>Sourced
  from <a href="https://github.com/pypa/setuptools/blob/main/NEWS.rst">setuptools's
  changelog</a>.</em></p> <blockquote> <h1>v78.1.1</h1> <h2>Bugfixes</h2> <ul> <li>More fully
  sanitized the filename in PackageIndex._download. (<a
  href="https://redirect.github.com/pypa/setuptools/issues/4946">#4946</a>)</li> </ul> </blockquote>
  </details> <details> <summary>Commits</summary> <ul> <li><a
  href="https://github.com/pypa/setuptools/commit/8e4868a036b7fae3208d16cb4e5fe6d63c3752df"><code>8e4868a</code></a>
  Bump version: 78.1.0 → 78.1.1</li> <li><a
  href="https://github.com/pypa/setuptools/commit/100e9a61ad24d5a147ada57357425a8d40626d09"><code>100e9a6</code></a>
  Merge pull request <a
  href="https://redirect.github.com/pypa/setuptools/issues/4951">#4951</a></li> <li><a
  href="https://github.com/pypa/setuptools/commit/8faf1d7e0ca309983252e4f21837b73ee12e960f"><code>8faf1d7</code></a>
  Add news fragment.</li> <li><a
  href="https://github.com/pypa/setuptools/commit/2ca4a9fe4758fcd39d771d3d3a5b4840aacebdf7"><code>2ca4a9f</code></a>
  Rely on re.sub to perform the decision in one expression.</li> <li><a
  href="https://github.com/pypa/setuptools/commit/e409e8002932f2b86aae7b1abc8f8c2ebf96df2c"><code>e409e80</code></a>
  Extract _sanitize method for sanitizing the filename.</li> <li><a
  href="https://github.com/pypa/setuptools/commit/250a6d17978f9f6ac3ac887091f2d32886fbbb0b"><code>250a6d1</code></a>
  Add a check to ensure the name resolves relative to the tmpdir.</li> <li><a
  href="https://github.com/pypa/setuptools/commit/d8390feaa99091d1ba9626bec0e4ba7072fc507a"><code>d8390fe</code></a>
  Extract _resolve_download_filename with test.</li> <li><a
  href="https://github.com/pypa/setuptools/commit/4e1e89392de5cb405e7844cdc8b20fc2755dbaba"><code>4e1e893</code></a>
  Merge <a href="https://github.com/jaraco/skeleton">https://github.com/jaraco/skeleton</a></li>
  <li><a
  href="https://github.com/pypa/setuptools/commit/3a3144f0d2887fa37c06550f42a101e9eebd953a"><code>3a3144f</code></a>
  Fix typo: <code>pyproject.license</code> -&gt; <code>project.license</code> (<a
  href="https://redirect.github.com/pypa/setuptools/issues/4931">#4931</a>)</li> <li><a
  href="https://github.com/pypa/setuptools/commit/d751068fd2627d6d8f1729e39cbcd8119049998f"><code>d751068</code></a>
  Fix typo: pyproject.license -&gt; project.license</li> <li>Additional commits viewable in <a
  href="https://github.com/pypa/setuptools/compare/v78.1.0...v78.1.1">compare view</a></li> </ul>
  </details> <br />

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can
  also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end)

---

<details> <summary>Dependabot commands and options</summary> <br />

You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this
  PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of
  the specified dependency - `@dependabot ignore <dependency name> major version` will close this
  group update PR and stop Dependabot creating any more for the specific dependency's major version
  (unless you unignore this specific dependency's major version or upgrade to it yourself) -
  `@dependabot ignore <dependency name> minor version` will close this group update PR and stop
  Dependabot creating any more for the specific dependency's minor version (unless you unignore this
  specific dependency's minor version or upgrade to it yourself) - `@dependabot ignore <dependency
  name>` will close this group update PR and stop Dependabot creating any more for the specific
  dependency (unless you unignore this specific dependency or upgrade to it yourself) - `@dependabot
  unignore <dependency name>` will remove all of the ignore conditions of the specified dependency -
  `@dependabot unignore <dependency name> <ignore condition>` will remove the ignore condition of
  the specified dependency and ignore conditions You can disable automated security fix PRs for this
  repo from the [Security Alerts page](https://github.com/bakerboy448/YNAmazon/network/alerts).

</details>

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Documentation

- Update README and add CONTRIBUTING.md
  ([`2bd551d`](https://github.com/bakerboy448/YNAmazon/commit/2bd551d01f69ae70cad18ef9710b0109affd5af3))

Reflect new error handling features (typed exceptions, retry logic, improved notifications) and add
  contribution guidelines.

### Features

- Amount tolerance matching, YNAB rate limit retry, CI coverage
  ([#5](https://github.com/bakerboy448/YNAmazon/pull/5),
  [`c6a2387`](https://github.com/bakerboy448/YNAmazon/commit/c6a23871448b2dd2f1bd3c0f132055bed2648b24))

## Summary - Fix index-0 bug where `if not 0` skipped valid matches at position 0 - Add configurable
  amount tolerance for fuzzy matching (default $2.00) - Add YNAB API rate limit retry with
  exponential backoff (60/120/240s) - Add payee caching to reduce API calls - Add pytest coverage
  reporting to CI

## Tests - 13 matching tests (exact, fuzzy, index-0 regression, boundary) - 7 rate limit retry tests
  (429 handling, auth errors, exhaustion)

## Test plan - [x] All 39 tests pass - [x] ruff check clean - [x] pyright 0 errors


## v0.8.0 (2026-03-12)

### Bug Fixes

- **tests**: Skip memo truncation tests when openai not installed and fix deptry mapping
  ([`191747f`](https://github.com/bakerboy448/YNAmazon/commit/191747f7cd3fe60827020fa9ccb8476e8f0dea5f))

Add pytest.importorskip("openai") so memo tests skip gracefully when openai isn't installed. Add
  deptry package_module_name_map for amazon-orders -> amazonorders.

### Documentation

- Add CI and license badges to README
  ([`0a69c53`](https://github.com/bakerboy448/YNAmazon/commit/0a69c53acc65b6d6804d823733e92b6c6974366c))

### Features

- Add custom User-Agent to all outgoing HTTP requests
  ([`de20674`](https://github.com/bakerboy448/YNAmazon/commit/de20674c5942912f2355449f6c8ee548ff39daa9))

Set YNAmazon/{version} user-agent on YNAB SDK, OpenAI, and GitHub API calls to identify the app in
  server logs and API analytics.

- Add retry_on_transient utility
  ([`206c010`](https://github.com/bakerboy448/YNAmazon/commit/206c0100a3ac8e46ac6151b9ea69fcb6760074fa))

Exponential backoff retry for TransientSyncError (5s, 10s, 20s). Non-transient exceptions propagate
  immediately.

- Add TransientSyncError and FatalSyncError exceptions
  ([`45c36df`](https://github.com/bakerboy448/YNAmazon/commit/45c36df8f69f145e1d21a9cd3aa73bfd44679d44))

Typed exceptions for differentiating retryable errors (network, 5xx) from fatal errors (auth, bad
  config) in the sync loop.

- Add typed error handling to daemon sync with retry and notification improvements
  ([`67a9730`](https://github.com/bakerboy448/YNAmazon/commit/67a973041af7f02bf8fd0afadeb1f0ecc543bdd2))

Replace generic except in _run_daemon_sync with typed handlers using retry_on_transient. Add
  notification retry, _build_error_message helper, and include partial sync progress in error
  notifications.

- Wrap errors in process_transactions with typed exceptions
  ([`383b23e`](https://github.com/bakerboy448/YNAmazon/commit/383b23e88727733b00b94f18f13fad15cd7dd933))

YNAB auth/service errors and Amazon auth/network errors are now wrapped as FatalSyncError or
  TransientSyncError. BadRequestException during YNAB update logs and continues instead of crashing.

### Testing

- Add error handling and retry tests
  ([`778f778`](https://github.com/bakerboy448/YNAmazon/commit/778f77895e4860dc764f153a8a137fa2f1e82ad8))

Tests for TransientSyncError/FatalSyncError exception classes and retry_on_transient exponential
  backoff logic.


## v0.7.1 (2026-02-26)

### Bug Fixes

- Standardize notification title prefix format
  ([`0ff63b9`](https://github.com/bakerboy448/YNAmazon/commit/0ff63b9957763bacf5d7c7f53617834984efc5c0))

Change "YNAmazon sync failed" to "YNAmazon: Sync failed" for consistent colon-separated prefix
  matching ynab-balance-monitor.

- Unblock build and fix CI pipeline
  ([`1d4e8e6`](https://github.com/bakerboy448/YNAmazon/commit/1d4e8e6e6508624bb79622ef4f3d0a60729c55d9))

- Override amazoncaptcha's pillow<9.6.0 constraint (upgraded to 12.1.1) - Fix CI workflow: add env
  vars for tests, install ai extra - Fix pyright type errors (SecretStr arg, schedule int cast,
  ignore placement) - Add tests/conftest.py with dummy env vars for test collection - Rewrite broken
  test_transactions.py to match refactored API - Auto-format all source files with ruff

### Documentation

- Add daemon mode and Apprise notifications to README
  ([`998588e`](https://github.com/bakerboy448/YNAmazon/commit/998588e5225743a5d75a545712698299028f2543))


## v0.7.0 (2026-02-24)

### Bug Fixes

- Address code review findings across all modules
  ([`52beced`](https://github.com/bakerboy448/YNAmazon/commit/52becedab478783ba49b309b4eac2469fd38e6b8))

- Protect TOTP secret and Apprise URLs with SecretStr - Sanitize exception logging to prevent API
  key leakage - Replace broad except Exception with specific handlers - Add HTTP timeout (30s) to
  requests.get calls - Fix float→Decimal in locate_amazon_transaction_by_amount - Replace Union[X,
  None] with X | None throughout - Add return type annotations to public methods - Add logging to
  YNAB transaction update operations - Use YNAB_MEMO_LIMIT constant instead of magic 500 - Replace
  lambda with proper function in daemon command - Remove commented-out dead code - Fix PEP 8 import
  ordering and blank lines in exceptions

### Chores

- Condense CLAUDE.md
  ([`a3f7dd0`](https://github.com/bakerboy448/YNAmazon/commit/a3f7dd0512f2ea9d87ae824459c3529832e210f4))

### Features

- Add Apprise notifications for daemon sync results
  ([`e5e253b`](https://github.com/bakerboy448/YNAmazon/commit/e5e253bf88645cb0dcdf2d9aa18c85e0f2a23375))

Sends Discord notifications via Apprise when daemon sync updates transactions or fails. No
  notification on zero-match runs to avoid noise.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>


## v0.6.0 (2026-02-10)

### Bug Fixes

- Remove unused timedelta import
  ([`0337909`](https://github.com/bakerboy448/YNAmazon/commit/033790992fe46ca384bbe518676daeabdcfc393c))

### Features

- **daemon**: Add --windows option for random time scheduling
  ([`37a1859`](https://github.com/bakerboy448/YNAmazon/commit/37a1859e73e603ca81b46408f48e944ed57037cc))

### Refactoring

- **daemon**: Extract helpers to reduce complexity
  ([`68f0aa9`](https://github.com/bakerboy448/YNAmazon/commit/68f0aa964aa0ac2ce0df40d61a6f154df7774d93))


## v0.5.0 (2026-02-02)

### Features

- Daemon mode automatically non-interactive
  ([`6b4b1af`](https://github.com/bakerboy448/YNAmazon/commit/6b4b1af6a3874bc6f4cc2358cae8e984219c02d1))

- Add non_interactive parameter to process_transactions() - Daemon mode passes non_interactive=True
  automatically - Settings NON_INTERACTIVE still works as fallback for manual runs - Consolidate
  date mismatch auto-accept logic


## v0.4.0 (2026-02-02)

### Features

- Add date mismatch tolerance and auto-accept settings
  ([`2ea17cd`](https://github.com/bakerboy448/YNAmazon/commit/2ea17cd768214c4a4937b0d699ebfd341bc04b5d))

- Add DATE_MISMATCH_TOLERANCE_DAYS setting (default: 0) to auto-accept date differences within N
  days - Add AUTO_ACCEPT_DATE_MISMATCH setting for daemon/non-interactive mode - Show date
  difference in days when mismatch occurs - Update README with new configuration options


## v0.3.0 (2026-02-02)

### Features

- Add configurable approved status filtering
  ([`f499471`](https://github.com/bakerboy448/YNAmazon/commit/f499471556431b271e6455a6374759fd9ef00402))

- Remove hardcoded `not t.approved` requirement that filtered out approved transactions - Add
  YNAB_APPROVED_STATUSES setting to control which approval statuses to match - Default to matching
  both approved and unapproved transactions - Update README with new configuration option


## v0.2.1 (2026-01-31)

### Bug Fixes

- Pass OTP secret key to AmazonSession for auto MFA
  ([`a881b0d`](https://github.com/bakerboy448/YNAmazon/commit/a881b0d33c5ac93e39f7360c23489db929fab3a1))


## v0.2.0 (2026-01-31)

### Continuous Integration

- Add multi-arch Docker build (amd64, arm64) and rebuild option
  ([`e21910b`](https://github.com/bakerboy448/YNAmazon/commit/e21910bb1263759eb8ee3e22fc2f915805111a66))

### Features

- Add daemon mode with Python-native scheduling
  ([`13bd679`](https://github.com/bakerboy448/YNAmazon/commit/13bd679c92c932b0d465b36311444d937fd5f7c8))

- Add `yna daemon` command for self-scheduling (default 20h, min 12h, max 48h) - Use `schedule`
  library for Python-native job scheduling - Remove supercronic dependency (simpler, no external
  binaries) - Container runs immediately on start, then at configured interval


## v0.1.0 (2026-01-31)

### Bug Fixes

- Add build deps for Pillow, improve cache path
  ([`42e77ae`](https://github.com/bakerboy448/YNAmazon/commit/42e77aec56026c4f39eae2f883486ff0227c83a4))

- Add zlib and jpeg dev libraries to builder stage for Pillow - Move cache from /tmp to
  ~/.cache/ynamazon for better security - Remove unused tempfile import

- Include README.md in Docker build context
  ([`2ccea02`](https://github.com/bakerboy448/YNAmazon/commit/2ccea02270ea9177fef28ea0fbd6cbfcc8930cf1))

- Reset to clean 0.1.0 version, fix semantic-release config for PEP 440
  ([`86d90fe`](https://github.com/bakerboy448/YNAmazon/commit/86d90fe8e0632beccdf2a0c23853ec16e30ed2f1))

- Resolve lint/type errors, add gitleaks pre-commit, fix Docker permissions
  ([`f80a8be`](https://github.com/bakerboy448/YNAmazon/commit/f80a8be87280eb2bf2abfc086ad6d05e8a098f7d))

- **ci**: Add system deps for Pillow build
  ([`c7bf1ef`](https://github.com/bakerboy448/YNAmazon/commit/c7bf1ef813f7cae13867713e15917ef44fcca8c9))

- **ci**: Use empty string for build_command, remove invalid version_toml
  ([`b66d9bc`](https://github.com/bakerboy448/YNAmazon/commit/b66d9bc57ce6e1c079859b34ae1759aaa7ccdb5e))

- **settings**: Do not enforce case-sensitivity for .env file settings
  ([`ceb411b`](https://github.com/bakerboy448/YNAmazon/commit/ceb411b6112c4e2312a77554cb44b5fe749f741e))

### Build System

- **amazonorders**: Add typings
  ([`cd5e328`](https://github.com/bakerboy448/YNAmazon/commit/cd5e3283935eb94d1d76f513f5f782e322dcb6cf))

### Chores

- **uv**: Use uv and clean up ynab_transactions
  ([`81164ac`](https://github.com/bakerboy448/YNAmazon/commit/81164acdbaf93044324a086f052e4b3bb3549bfd))

### Code Style

- **type-hinting**: Adjust return type of `get_ynab_transactions` to match possible values
  ([`e187b88`](https://github.com/bakerboy448/YNAmazon/commit/e187b889493c658a45c200ecb71012e51ff65075))

ignore E501 linting rule as suggested by ruff when using their formatter
  (https://docs.astral.sh/ruff/formatter/#conflicting-lint-rules)

### Continuous Integration

- Add concurrency, OCI labels, manual-only triggers
  ([`d29844f`](https://github.com/bakerboy448/YNAmazon/commit/d29844f5e049d4566d724193241827c142e1fa30))

- Add GitHub Actions CI, semantic release, and GHCR build
  ([`0dd331f`](https://github.com/bakerboy448/YNAmazon/commit/0dd331f3b217ca6c732161b07ee8bb54c055772c))

- Add CI workflow with lint, typecheck, and build jobs - Add release workflow with auto pre-release
  on push - Add manual release trigger via workflow_dispatch - Add conventional commits pre-commit
  hook - Add pyright to dev dependencies - Configure python-semantic-release

- Disable build in semantic-release (Docker handles it)
  ([`42dcc64`](https://github.com/bakerboy448/YNAmazon/commit/42dcc64c7da725b48cab480d7dc946e8c61a0b5c))

- Make lint/typecheck non-blocking (existing errors)
  ([`369f67e`](https://github.com/bakerboy448/YNAmazon/commit/369f67e4d9d7e2dbfc99669dbdf436aa975f1d63))

- Release only on manual dispatch, not every commit
  ([`5d3063c`](https://github.com/bakerboy448/YNAmazon/commit/5d3063c596708abef0865aca785fa7a19fea2af7))

### Documentation

- Add logging config to compose example, document OTP setup
  ([`8b67d31`](https://github.com/bakerboy448/YNAmazon/commit/8b67d3194196b4684bccbab9becef89db60152a1))

- Rewrite README with Docker usage and new features
  ([`f0f010c`](https://github.com/bakerboy448/YNAmazon/commit/f0f010c9328f80935e380a660ff335285de67276))

- **cli**: Correct script name in docs and add a pop of **color**
  ([`319b61a`](https://github.com/bakerboy448/YNAmazon/commit/319b61a8d8277a1e2e271652324135d4e358263e))

- **cli**: Update docs to reflect typer cli and fix some issues with deps and deptry
  ([`d026659`](https://github.com/bakerboy448/YNAmazon/commit/d0266595a8d75bc33389edd931870c4b180ec842))

### Features

- Add --days, --dry-run options and Docker support
  ([`fa63296`](https://github.com/bakerboy448/YNAmazon/commit/fa632960f0ae264822d55ab310b71bee1fae48cc))

- Add --force option, date filtering, and cap days at 31
  ([`4d7127d`](https://github.com/bakerboy448/YNAmazon/commit/4d7127d72795c551020833823a78a2675289bc43))

- Add --force flag to process all transactions (including approved with memos) - Add date filtering
  to YNAB transactions based on --days parameter - Cap --days at 31 max (Amazon API limitation) -
  Add transaction_days to AmazonConfig for proper parameter passing - Fix process_memo import (was
  duplicated, causing openai import error) - Convert memo to string when AI processing unavailable

- Add AMAZON_DEBUG env var for browser automation logging
  ([`b09ffbf`](https://github.com/bakerboy448/YNAmazon/commit/b09ffbf8e25346956f5ac21660f7e04a4805e59f))

- Add amazon_full_details setting for optional item prices
  ([`1d9352b`](https://github.com/bakerboy448/YNAmazon/commit/1d9352bb1549d0e55e644875d1eb8008a5404db2))

- Add match_empty_memo option to match Amazon transactions with blank memo
  ([`1072874`](https://github.com/bakerboy448/YNAmazon/commit/1072874c82efee70e73278ff136deb0578197c03))

- Optimize Docker, add diff output, config file support
  ([`ad38c5f`](https://github.com/bakerboy448/YNAmazon/commit/ad38c5ff59f5569d8f9743870940b160d328a542))

- Remove hardcoded UID 1000 from Dockerfile - Add pip install with --no-cache-dir - Clean apt cache
  properly - Add unified diff output for --dry-run mode - Support multiple config file paths
  (/app/config/.env, .env) - Add docker-compose.example.yml

- **amazon-orders**: Add util for checking integration test of amazon-orders as a sort of
  integration test for ynamazon
  ([`51d720e`](https://github.com/bakerboy448/YNAmazon/commit/51d720e0eb898c9a3d06cf711faa4c0145a05e58))

checks the latest workflow run to see if it was successful; could be included in our own integration
  test?

- **amazon-orders**: Add util for checking integration test of amazon-orders as a sort of
  integration test for ynamazon
  ([`47a7cf9`](https://github.com/bakerboy448/YNAmazon/commit/47a7cf9e9d0c7d5a39541487f3f52c9fc8d05858))

checks the latest workflow run to see if it was successful; could be included in our own integration
  test?

- **cli**: True "cli" with documented arguments
  ([`3206f40`](https://github.com/bakerboy448/YNAmazon/commit/3206f40e95fb93dfd8d847e501cd14e864ff06e2))

restructure files to keep modules better organized, more complete pyproject.toml

### Refactoring

- Simplify memo format to 'Item A, Item B | Order #XXX'
  ([`f8a43c0`](https://github.com/bakerboy448/YNAmazon/commit/f8a43c0d0d546badd5e4a214b235b18e2cdb826f))

- **RootModel**: Use RootModel for Transactions and Payees
  ([`6505491`](https://github.com/bakerboy448/YNAmazon/commit/65054918c80a7a06bd1235a984bda23e20403484))

### Testing

- **faker**: Add faker as a non-transitive dependency
  ([`568cf92`](https://github.com/bakerboy448/YNAmazon/commit/568cf9221b957fb453b15f724e93605ade773031))

- **tox**: Add tox for testing across multiple versions of python
  ([`c6807ef`](https://github.com/bakerboy448/YNAmazon/commit/c6807ef1062269bcfc9ef96c3ea1b87a210ff575))

changes made to packages to support older versions of python; all changes were purely type-hinting
  related

- **transactions**: Some tests created and passing
  ([`388bca4`](https://github.com/bakerboy448/YNAmazon/commit/388bca4435d2570026418433d241a28d08c7b3e4))

- **transactions**: Some tests created and passing
  ([`0eba199`](https://github.com/bakerboy448/YNAmazon/commit/0eba199c098be5aadb2675afd489f4a76a29b0d4))
