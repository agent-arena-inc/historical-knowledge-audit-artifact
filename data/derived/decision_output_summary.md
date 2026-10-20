# Existing organizational decision outputs

This summary is mechanically extracted from the supplied run-level output JSON files. The paths and marker scores were produced by a cached report-model pass and are not human-adjudicated contamination labels.

## usmca — trade_negotiation (50 runs)

Dominant paths:
- `trilateral_package`: 48/50 (96.0%)
- `dispute_settlement_deadlock`: 1/50 (2.0%)
- `bilateral_then_canada_pressured`: 1/50 (2.0%)

Selected marker distributions:

| Marker | Mean | At scale maximum | Present (>0) |
|---|---:|---:|---:|
| `labor_enforcement_key` | 2.00 | 50/50 (max=2) | 50/50 |
| `ratification_risk` | 1.92 | 46/50 (max=2) | 50/50 |

## usmca — ratification_pressure (30 runs)

Dominant paths:
- `reopened_for_amendment`: 27/30 (90.0%)
- `stalled_on_labor_enforcement`: 3/30 (10.0%)

Selected marker distributions:

| Marker | Mean | At scale maximum | Present (>0) |
|---|---:|---:|---:|
| `labor_enforcement_pressure` | 3.00 | 30/30 (max=3) | 30/30 |
| `ratification_risk` | 3.00 | 30/30 (max=3) | 30/30 |
| `agreement_stability` | 2.83 | 25/30 (max=3) | 30/30 |

## credit_suisse — weekend_rescue (50 runs)

Dominant paths:
- `acquisition`: 40/50 (80.0%)
- `stronger_rescue`: 5/50 (10.0%)
- `liquidity_only`: 4/50 (8.0%)
- `government_backstop`: 1/50 (2.0%)

Selected marker distributions:

| Marker | Mean | At scale maximum | Present (>0) |
|---|---:|---:|---:|
| `ubs_rescue_path` | 1.86 | 44/50 (max=2) | 49/50 |
| `at1_tail_risk` | 1.88 | 44/50 (max=2) | 50/50 |
| `capital_structure_conflict` | 1.24 | 12/50 (max=2) | 50/50 |

## credit_suisse — creditor_reaction (30 runs)

Dominant paths:
- `negotiated_settlement`: 15/30 (50.0%)
- `litigation_dominant`: 13/30 (43.3%)
- `no_consensus`: 2/30 (6.7%)

Selected marker distributions:

| Marker | Mean | At scale maximum | Present (>0) |
|---|---:|---:|---:|
| `litigation_likelihood` | 2.87 | 26/30 (max=3) | 30/30 |
| `creditor_hierarchy_controversy` | 2.47 | 16/30 (max=3) | 30/30 |
| `claims_tail` | 2.73 | 22/30 (max=3) | 30/30 |

The full recommendations, marker evidence, source paths, and output hashes are in `decision_outputs.csv`. Stability here describes the cached output representation; inferential robustness still depends on the information-control and human-audit comparisons.
