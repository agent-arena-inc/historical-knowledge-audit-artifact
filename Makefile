PYTHON ?= python3
SOURCE_ROOT ?= $(if $(wildcard data/cases),data/cases,../AgentArena/demos)
VERIFY_MODE := $(if $(wildcard data/annotations/private_sample_key.csv),,--release-mode)

.PHONY: manifest instruments table decisions verify all

manifest:
	$(PYTHON) scripts/build_run_manifest.py --source-root "$(SOURCE_ROOT)"

instruments:
	$(PYTHON) scripts/freeze_audit_instruments.py --source-root "$(SOURCE_ROOT)"

table:
	$(PYTHON) scripts/reproduce_provisional_table.py --source-root "$(SOURCE_ROOT)"

decisions:
	$(PYTHON) scripts/extract_decision_outputs.py --source-root "$(SOURCE_ROOT)"

verify:
	$(PYTHON) scripts/verify_artifact.py $(VERIFY_MODE) --source-root "$(SOURCE_ROOT)"

all: manifest instruments table decisions verify
