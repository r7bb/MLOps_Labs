# GitHub Actions Lab: Currency Converter

A currency converter tested with **pytest** and **unittest**, with both test suites running automatically through **GitHub Actions** on every push to `main`.

Based on [GitHub Lab 1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1) from Prof. Ramin Mohammadi's MLOps repo.

## Modifications from Original

| Original Lab | This Lab |
|---|---|
| `calculator.py` with arithmetic functions | `converter.py` with currency conversion functions |
| 4 functions (fun1 to fun4) | 4 functions: `supported_currencies`, `get_rate`, `convert`, `convert_to_many` |
| 4 tests per file | 14 pytest tests and 10 unittest tests |
| Type checks on inputs | Also rejects negative amounts and unsupported currencies |
| Tests cover expected values only | Tests also cover edge cases and error handling |
| Python 3.8, actions v2 | Python 3.10, current action versions |

Exchange rates are fixed sample values (per 1 USD) so the tests always give the same result.

## Functions

| Function | Description |
|---|---|
| `supported_currencies()` | Returns the supported currency codes |
| `get_rate(from, to)` | Returns the exchange rate between two currencies |
| `convert(amount, from, to)` | Converts an amount, rounded to 2 decimals |
| `convert_to_many(amount, from, [to, ...])` | Converts one amount into several currencies |

## Run Locally

```bash
cd github_lab
pip install -r requirements.txt
python -m pytest test/test_pytest.py -v
python -m unittest test.test_unittest -v
```

## GitHub Actions

- `pytest_action.yml` runs the pytest suite and uploads the XML test report as an artifact
- `unittest_action.yml` runs the unittest suite

Results are in the **Actions** tab.
