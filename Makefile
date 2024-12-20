LIBRARY = pyggdrasil
TESTS = tests

.PHONY: test typecheck lint format pretty check build publish

test: T="$(TESTS)"
test:
	poetry run pytest "$(T)"

typecheck:
	poetry run mypy "$(LIBRARY)" --strict

lint:
	poetry run ruff check --fix "$(TESTS)"
	poetry run ruff check --fix "$(LIBRARY)"

format:
	poetry run isort "$(TESTS)"
	poetry run isort "$(LIBRARY)"
	poetry run black "$(TESTS)"
	poetry run black "$(LIBRARY)"

check: lint typecheck

publish: VERSION=$(shell poetry version -s)
publish:
	git add .
	git commit --allow-empty -m "v${VERSION}"
	git tag -a "v${VERSION}" -m "v${VERSION}"
	git push --follow-tags
	poetry publish --build
