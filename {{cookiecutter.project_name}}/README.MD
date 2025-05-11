# {{ cookiecutter.project_name }}

This cookiecutter sets up a basic python environment. Specifically, it holds the configuration for:

- ruff (linter)
- pre-commit (git hooks manager)
- black (formmater)
- isort (formatter)
- github actions (linting workflow)

In this README you will also find some useful commands.

<!-- FIRST STEPS -->
## Setup Environment

1. Create conda environment:
```
conda env create -f environment.yaml
```
2. Install pre-commit hooks
```
pre-commit install
```

For more information about the available tools, check the README.MD in the root directory.

You are all Set! :rocket:

<!-- END FIRST STEPS -->

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

## 🛠 Hydra Configuration Structure

This project uses [Hydra](https://hydra.cc) to manage configurations in a structured, modular, and composable manner. Hydra enables easy experimentation, hyperparameter tuning, and separation of concerns between components like the model, training loop, and runtime settings.

To run with default configs:

```bash
python main.py
```
To override a value:
```bash
python main.py model.hidden_dim=256
```
### 📁 Directory Layout

Hydra configurations are stored under the `configs/` directory with a clear separation between different concerns:

configs/
├── config.yaml # Root configuration entry point
├── model/
│ └── mlp.yaml # Model-specific configuration
├── training/
│ └── default.yaml # Training hyperparameters


### 📌 Configuration Structure

- `config.yaml`: Root config that defines the defaults and entry point. It imports all other configurations.
- `model/mlp.yaml`: Defines model-specific parameters such as hidden dimensions, dropout rate, and activation function.
- `training/default.yaml`: Contains training hyperparameters like `batch_size`, `epochs`, and general runtime options (e.g., `seed`, `use_gpu`).


### 🧩 Why Structure Matters

Keeping configurations **modular and organized** improves maintainability and reproducibility:

- You can independently modify model, training, or logging settings.
- You avoid deeply nested or hard-coded settings in code files.
- It becomes easier to compare experiments or set up sweeps.


### 🔄 Overriding Configurations

Hydra supports **runtime overrides** from the command line. You can modify any setting without changing the base config files:

```bash
python main.py training.batch_size=128 model.hidden_dim=512
```
You can also override entire config files:
```
python main.py model=cnn training=fast
```
This composability is one of Hydra’s strongest features—use it to keep your experiments clean, trackable, and reproducible.

### ✅ Next Steps

Once your configs are in place:

    Define new model/, training/, or other component files as needed.

    Use the @hydra.main decorator in your entry script to load the configuration.

    Rely on the DictConfig object (from omegaconf) to access all parameters inside your application logic.



## References

Linting with Ruff (https://docs.astral.sh/ruff)
Formatting with Isort (https://pycqa.github.io/isort/)
Formatting with Black (https://github.com/psf/black)
Managing git hooks with pre-commit (https://pre-commit.com/)
Implementing CI/CD with Github Actions (https://github.com/features/actions)


### Other (Not installed)

If need be, there is a library for typos available using rust's package manager cargo.

typos detection in source code: (https://github.com/crate-ci/typos)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
