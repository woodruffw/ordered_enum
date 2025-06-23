ALL_PY_SRCS := $(shell find src -name '*.py') \
	$(shell find test -name '*.py')

.PHONY: all
all:
	@echo "Run my targets individually!"

.PHONY: dev
dev:
	uv venv
	uv pip install -e .[dev]

.PHONY: lint
lint:
	uv run black $(ALL_PY_SRCS) && \
	uv run isort $(ALL_PY_SRCS) && \
	uv run flake8 $(ALL_PY_SRCS) && \
	git diff --exit-code

.PHONY: test
test:
	uv run -m coverage run -m pytest
	uv run -m coverage report -m --fail-under 100

.PHONY: package
package:
	uv run -m build

.PHONY: edit
edit:
	$(EDITOR) $(ALL_PY_SRCS)
