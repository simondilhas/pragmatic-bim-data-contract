# Classifications Integration

## Repository

- Canonical source repository: `simondilhas/pragmatic-bim-classifications` (private)
- Consumer path: `external/classifications`

## Add and Update Submodule

```bash
git submodule add git@github.com:simondilhas/pragmatic-bim-classifications.git external/classifications
git submodule update --init --recursive
```

Update to latest:

```bash
git submodule update --remote --recursive
```

Pin to a specific tag:

```bash
cd external/classifications
git fetch --tags
git checkout v2026.03
cd ../..
git add external/classifications .gitmodules
git commit -m "Pin classifications submodule to v2026.03"
```

## URI Convention

Use GitHub Raw URLs for published metadata references:

`https://raw.githubusercontent.com/simondilhas/pragmatic-bim-classifications/<ref>/<path>`

- Use tags for stable references.
- Use `main` only for development links.

## CI Authentication for Private Submodule

Use a read-only token with `repo` scope.

Example GitHub Actions bootstrap:

```yaml
- name: Checkout
  uses: actions/checkout@v4
  with:
    submodules: recursive
    token: ${{ secrets.CLASSIFICATIONS_READ_TOKEN }}
```

Alternative explicit setup:

```yaml
- name: Configure GitHub token for private submodules
  run: git config --global url."https://${{ secrets.CLASSIFICATIONS_READ_TOKEN }}@github.com/".insteadOf "https://github.com/"

- name: Init submodules
  run: git submodule update --init --recursive
```
