# Test B: external ZIP execution record

The returned terminal log records a successful execution of the five Level-1
recomputation and verification commands from an extracted reviewer ZIP.

- Recorded execution time: 2026-10-28 23:33:30 +08:00.
- Environment evidence: Windows-style output paths and `python3` commands.
  OS version and Python version were not recorded.
- Distribution: extracted ZIP, according to the test handoff and working path.
- Result: exit code 0; elapsed time 23 seconds.
- [Original returned terminal log](terminal_output_B.txt), preserved byte-for-byte.
- Log SHA-256: `f7886d0bfde5a85b6322f7320c39aa65052dfd7056efd55ebd95c7f865f41791`.

| Step | Observed output |
|---|---|
| Build run manifest | 286 rows; 280 candidate runs |
| Freeze audit instruments | 2 case instruments |
| Reproduce provisional table | 12 rows |
| Extract decision outputs | 160 run-level outputs |
| Verify release artifact | `artifact verification passed` |

## Scope and version limits

This is one reported external-user execution and supports the usability of the
Level-1 ZIP instructions for that execution. It does not establish independent
human validation of the research results or Level-2/Level-3 reproducibility.

The returned log does not record the tested commit SHA or ZIP checksum, so the
exact tested revision cannot be established from this log alone. Its timestamp
precedes the subsequent anonymity-checker repair; it is not evidence that the
external tester reran the repaired release. The repaired release is separately
validated by the repository's local rebuild and GitHub Actions checks.
