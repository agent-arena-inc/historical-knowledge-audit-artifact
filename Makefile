PYTHON ?= python3
SOURCE_ROOT ?= ../case_source

.PHONY: manifest instruments table verify all

manifest:
	$(PYTHON) scripts/build_run_manifest.py --source-root "$(SOURCE_ROOT)"

instruments:
	$(PYTHON) scripts/freeze_audit_instruments.py --source-root "$(SOURCE_ROOT)"

table:
	$(PYTHON) scripts/reproduce_provisional_table.py --source-root "$(SOURCE_ROOT)"

verify:
	$(PYTHON) scripts/verify_artifact.py --source-root "$(SOURCE_ROOT)"

all: manifest instruments table verify
