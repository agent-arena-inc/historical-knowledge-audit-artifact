# Provisional cached-judgment counts

These counts are mechanically recomputed from cached model judgments. They are not human-verified leakage rates.

| Case | Condition | Evaluator | Corpus | Attempted | Valid | Score >= 2 | Missing | Parse failures | Keyword-positive |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| usmca | historical_case | cached_anthropic_report_judge | 50 | 50 | 50 | 22 | 0 | 0 | 9 |
| usmca | historical_case | cached_anthropic_haiku_judge | 50 | 49 | 49 | 0 | 1 | 0 | 13 |
| usmca | historical_case | cached_openai/gpt-5.5 | 50 | 49 | 48 | 5 | 1 | 1 | 13 |
| usmca | historical_case | cached_google/gemini-3.1-pro-preview | 50 | 49 | 48 | 11 | 1 | 1 | 13 |
| credit_suisse | historical_case | cached_anthropic_report_judge | 50 | 50 | 50 | 0 | 0 | 0 | 0 |
| credit_suisse | control | cached_anthropic_report_judge | 4 | 4 | 4 | 0 | 0 | 0 | 0 |
| credit_suisse | hindsight_control | cached_anthropic_report_judge | 5 | 5 | 5 | 0 | 0 | 0 | 1 |
| credit_suisse | seeded_positive_control | cached_anthropic_report_judge | 5 | 5 | 5 | 1 | 0 | 0 | 1 |
| credit_suisse | historical_case | cached_openai/gpt-5.5 | 50 | 50 | 50 | 0 | 0 | 0 | 0 |
| credit_suisse | seeded_positive_control | cached_openai/gpt-5.5 | 5 | 5 | 5 | 4 | 0 | 0 | 1 |
| credit_suisse | historical_case | cached_google/gemini-3.1-pro-preview | 50 | 50 | 50 | 0 | 0 | 0 | 0 |
| credit_suisse | seeded_positive_control | cached_google/gemini-3.1-pro-preview | 5 | 5 | 5 | 2 | 0 | 0 | 1 |

Do not cite this table as a validated false-negative rate. Denominators, prompt versions, and human labels must be reconciled first.
