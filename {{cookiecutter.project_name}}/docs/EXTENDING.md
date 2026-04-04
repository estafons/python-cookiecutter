# Extending the template

This file explains the **best way** to add a new dataset, model, or experiment.

## Add a new dataset

### 1. Add a config file
Create a new config:
```text
configs/data/dataset_c.yaml
```

Example:
```yaml
name: dataset_c
builder: dataset_c
root: ${paths.data_dir}/dataset_c
num_classes: 5
input_dim: 128
```

### 2. Add dataset-building logic
Edit:
```text
src/{{ cookiecutter.package_name }}/data/factory.py
```

Add a new branch in `build_data(cfg)` that knows how to prepare the dataset.

### 3. Keep the interface stable
Every dataset should return the same kind of object, for example:
- `train_data`
- `test_data`
- metadata such as `num_classes`

That keeps the training and testing code generic.

### Best practice
Do **not** create a new training script for each dataset. Add the dataset behind the same factory and select it through Hydra.

---

## Add a new model

### 1. Add a config file
Create:
```text
configs/model/new_model.yaml
```

Example:
```yaml
name: new_model
builder: new_model
hidden_dim: 256
```

### 2. Add the implementation
Create:
```text
src/{{ cookiecutter.package_name }}/models/new_model.py
```

### 3. Register it in the model factory
Edit:
```text
src/{{ cookiecutter.package_name }}/models/factory.py
```

Add a new branch in `build_model(cfg)`.

### Best practice
Keep all models behind the same interface:
- input: config + dataset metadata
- output: a model object with the same public methods expected by `train.py` and `test.py`

Do **not** special-case every model in `main.py`.

---

## Add a new experiment

### 1. Create a named experiment config
Create:
```text
configs/experiment/new_experiment.yaml
```

Example:
```yaml
# @package _global_

defaults:
  - override /model: new_model
  - override /data: dataset_c

task: train
tags: ["new_model", "dataset_c"]
```

### 2. Run it
```bash
python main.py experiment=new_experiment logger=wandb
```

### Best practice
Use `configs/experiment/` for:
- canonical comparisons
- ablations
- paper-ready settings
- reproducible reruns

Use CLI overrides for quick one-off tests.

---

## When should I use CLI overrides vs experiment files?

### Use CLI overrides for:
- quick debugging
- trying one or two hyperparameters
- temporary tests

Example:
```bash
python main.py model.hidden_dim=512 trainer.max_epochs=5
```

### Use experiment files for:
- anything you will want to rerun later
- comparisons you want to track in W&B
- settings that may appear in reports, slides, or papers

---

## What not to do

Avoid these patterns:
- `train_dataset_a.py`
- `train_baseline.py`
- `test_model_b.py`

They do not scale and make comparison harder.

The preferred pattern is:
- one generic pipeline
- Hydra chooses the combination
- W&B records the run
