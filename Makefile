ALL_PY_SRCS := $(shell find src -name '*.py') \
	$(shell find test -name '*.py')

.PHONY: all
all:
	@echo "Run my targets individually!"

.PHONY: dev
dev:
	test -d env || python3 -m venv env
	. env/bin/activate && pip install -e .[dev]

.PHONY: lint
lint:
	. env/bin/activate && \
		black $(ALL_PY_SRCS) && \
		isort $(ALL_PY_SRCS) && \
		flake8 $(ALL_PY_SRCS) && \
		git diff --exit-code

.PHONY: test
test:
	./env/bin/python -m coverage run -m pytest
	./env/bin/python -m coverage report -m --fail-under 100

.PHONY: package
package:
	./env/bin/python -m build

.PHONY: edit
edit:
	$(EDITOR) $(ALL_PY_SRCS)
