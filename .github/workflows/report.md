# Research Report — Hardcoded Secret Detection (PoC)

## Summary
- Date: 2025-10-03
- Target: sample config in repo
- Issue: hard-coded credentials present in `app/config.py` (dummy values)
- PoC: GitHub Actions scanner flags the line and uploads `scan-results.log`.

## Remediation
- Remove secrets from code and use secret stores (GitHub Secrets / Key Vault).
- Add pre-commit hooks (detect-secrets) and SAST tools (CodeQL).
