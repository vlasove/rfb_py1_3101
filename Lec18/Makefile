.PHONY: format, lint, check

format:
	black example_b.py && docformatter -i example_b.py && isort example_b.py

lint:
	pylint example_b.py

check:
	mypy example_b.py

.DEFAULT_GOAL := format