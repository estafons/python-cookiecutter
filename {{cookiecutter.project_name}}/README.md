# {{ cookiecutter.project_name }}

A minimal, task-aware research template built around:

- **Hydra** for configuration
- **Weights & Biases** for experiment tracking
- **task-oriented structure** for extending the project safely

This template is designed around a key idea:

> A new **dataset format** usually means a new **task**.

For example:
- `item, label` → classification or regression
- `item1, item2` → pairwise / matching / contrastive task

That means the project is organized so that:
- datasets belong to a **task**
- models belong to a **task**
- training and testing logic belong to a **task**
- named experiments compose `task + model + data`

This keeps the codebase clean when your project grows.

For detailed usage, see:
- [`docs/USE_CASES.md`](docs/USE_CASES.md)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

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

5. (Optional) configure W&B:
```bash
wandb login
```
<!-- END FIRST STEPS -->

## What this template includes

- Hydra config groups for:
  - `task`
  - `model`
  - `data`
  - `experiment`
  - `logger`
  - `trainer`
  - `paths`
- W&B logging, with **offline mode as the default**
- a task dispatcher so `classification` and future tasks like `regression` or `pairwise` can coexist cleanly
- practical docs centered on use cases

## Recommended mental model

Use this split consistently:

- `main.py` = orchestration only
- `configs/task/` = what kind of problem this is
- `configs/model/` = which model to use for that task
- `configs/data/` = which dataset to use for that task
- `src/{{ cookiecutter.package_name }}/tasks/` = task-specific train/test logic
- `src/{{ cookiecutter.package_name }}/models/` = model implementations
- `src/{{ cookiecutter.package_name }}/data/` = dataset builders

## Why tasks matter

You are right to separate:
- `item, label`
- `item1, item2`

as different tasks.

I agree with that approach.

Even if both are called “learning,” they usually differ in:
- dataset sample format
- model forward signature
- loss function
- metrics
- batching/collation
- train/test logic

Trying to force both through one training loop usually makes the architecture worse.

## Example commands

### Default run
```bash
python main.py
```

### Train baseline classifier on dataset A
```bash
python main.py task=classification model=baseline_classifier data=dataset_a task_config.name=classification logger=wandb
```

### Train CLIP linear classifier on dataset B
```bash
python main.py task=classification model=clip_linear_classifier data=dataset_b logger=wandb
```

### Run a named experiment
```bash
python main.py experiment=clip_dataset_b logger=wandb
```

### Override a hyperparameter quickly
```bash
python main.py model.hidden_dim=256 trainer.max_epochs=20
```
