# CHANGELOG


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
