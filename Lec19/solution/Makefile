.PHONY: format, lint, check

format:
	black main.py && docformatter -i main.py && isort main.py

lint:
	pylint main.py

check:
	mypy main.py

.DEFAULT_GOAL := format