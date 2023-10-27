# {{ cookiecutter.project_name }}

This cookiecutter sets up a basic python environment. Specifically, it holds the configuration for:

- ruff (linter)
- pre-commit (git hooks manager)
- black (formmater)
- isort (formatter)
- github actions (linting workflow)

In this README you will also find some useful commands.

## Setup Dev Environment

1. Install dependencies
```
pip install -r requirements-dev.txt
```
2. Install pre-commit hooks
```
pre-commit install
```

You are all Set! :rocket:

## Usefull Commands

### Running tools from the command line

#### Ruff

From the command line:

```
ruff check --select=E,T201 .
ruff check --select=ALL .
```

#### isort

```
isort .
```

#### Black

```
black .
```
Show what black will change without making changes:
```
black . --diff
```

#### Pre-commit

Install hooks specified in config file:
```
pre-commit install
```

commit without running hooks:
```
git commit -m "<some message>" --no-verify
```

Run hooks without need for commit:
```
pre-commit run --all-files
```


## References

Linting with Ruff (https://docs.astral.sh/ruff)
Formatting with Isort (https://pycqa.github.io/isort/)
Formatting with Black (https://github.com/psf/black)
Managing git hooks with pre-commit (https://pre-commit.com/)
Implementing CI/CD with Github Actions (https://github.com/features/actions)


### Other (Not installed)

If need be, there is a library for typos available using rust's package manager cargo.

typos detection in source code: (https://github.com/crate-ci/typos)
