# {{ cookiecutter.project_name }}

A minimal research template for **Hydra-managed experiments** with **Weights & Biases logging**.

This template is intentionally small, but it already supports the most common research comparison setup:

- **2+ models** through `configs/model/`
- **2+ datasets** through `configs/data/`
- **named experiments** through `configs/experiment/`
- **train/test switching** through a single `task` flag
- **W&B logging** through `configs/logger/`

Use this repository as a framework for **reproducible experiments**, not as a collection of scripts.

For the initial setup, see the section below. For how to add new datasets, models, or experiments, see:
- [`docs/WORKFLOW.md`](docs/WORKFLOW.md)
- [`docs/EXTENDING.md`](docs/EXTENDING.md)

<!-- FIRST STEPS -->
## Initial setup

1. Create the environment:
```bash
conda env create -f environment.yaml
```

2. Activate it:
```bash
conda activate {{ cookiecutter.project_name }}
```

3. Install the project in editable mode:
```bash
pip install -e .
```

4. Install pre-commit hooks:
```bash
pre-commit install
```
<!-- END FIRST STEPS -->

## What this template includes

- **Hydra** for modular configuration
- **W&B** for experiment tracking, config logging, and output organization
- **Ruff**, **Black**, and **isort** for code quality
- **pre-commit** for automatic checks before commit
- a minimal `src/` layout that keeps implementation separate from configuration

## Recommended mental model

Use this split consistently:

- `main.py` = orchestration only
- `configs/` = experiment definition
- `src/{{ cookiecutter.package_name }}/` = implementation

Do **not** create separate scripts like:
- `train_baseline_dataset1.py`
- `train_model2_dataset2.py`

Instead, compose runs with Hydra:
```bash
python main.py model=baseline data=dataset_a task=train
python main.py model=my_model data=dataset_b task=test ckpt_path=/path/to/checkpoint
python main.py experiment=my_model_dataset_b logger=wandb
```

## Project layout

```text
.
├── configs/
│   ├── config.yaml
│   ├── data/
│   │   ├── dataset_a.yaml
│   │   └── dataset_b.yaml
│   ├── experiment/
│   │   ├── baseline_dataset_a.yaml
│   │   ├── baseline_dataset_b.yaml
│   │   ├── my_model_dataset_a.yaml
│   │   └── my_model_dataset_b.yaml
│   ├── logger/
│   │   ├── none.yaml
│   │   └── wandb.yaml
│   ├── model/
│   │   ├── baseline.yaml
│   │   └── my_model.yaml
│   ├── paths/
│   │   └── default.yaml
│   └── trainer/
│       └── default.yaml
├── docs/
│   ├── EXTENDING.md
│   └── WORKFLOW.md
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── data/
│       ├── models/
│       ├── run.py
│       ├── train.py
│       ├── test.py
│       └── utils/
├── environment.yaml
├── main.py
└── pyproject.toml
```

## Common commands

### Run the default configuration
```bash
python main.py
```

### Train a specific model on a specific dataset
```bash
python main.py model=baseline data=dataset_a task=train logger=wandb
python main.py model=my_model data=dataset_b task=train logger=wandb
```

### Test using a saved checkpoint
```bash
python main.py model=baseline data=dataset_a task=test ckpt_path=/path/to/checkpoint logger=wandb
```

### Run a named experiment
```bash
python main.py experiment=my_model_dataset_b logger=wandb
```

### Override hyperparameters at runtime
```bash
python main.py model.hidden_dim=256 trainer.max_epochs=20
```

## Code-quality tools

### Ruff
```bash
ruff check --select=E,T201 .
ruff check --select=ALL .
ruff check . --fix
```

### isort
```bash
isort .
```

### Black
```bash
black .
black . --diff
```

### pre-commit
```bash
pre-commit install
pre-commit run --all-files
git commit -m "message" --no-verify
```
