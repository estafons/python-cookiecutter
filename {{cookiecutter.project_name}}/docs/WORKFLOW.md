# Workflow guide

This project is built around **config composition**.

## The four things you choose for each run

1. **Model**: which method are you running?
   - `configs/model/baseline.yaml`
   - `configs/model/my_model.yaml`

2. **Dataset**: what data are you using?
   - `configs/data/dataset_a.yaml`
   - `configs/data/dataset_b.yaml`

3. **Task**: are you training or testing?
   - `task=train`
   - `task=test`

4. **Experiment**: is this a named run you want to reproduce?
   - `configs/experiment/*.yaml`

## Why this structure is good

It lets you compare:
- baseline on dataset A
- baseline on dataset B
- your model on dataset A
- your model on dataset B

without creating separate scripts for each combination.

## Typical usage

### 1. Train baseline on dataset A
```bash
python main.py model=baseline data=dataset_a task=train logger=wandb
```

### 2. Train your model on dataset B
```bash
python main.py model=my_model data=dataset_b task=train logger=wandb
```

### 3. Test a trained checkpoint
```bash
python main.py model=my_model data=dataset_b task=test ckpt_path=/path/to/checkpoint logger=wandb
```

### 4. Re-run a named experiment
```bash
python main.py experiment=my_model_dataset_b logger=wandb
```

## What goes where

### `configs/`
Contains everything that changes between experiments:
- model choice
- dataset choice
- trainer settings
- paths
- logger setup
- named experiments

### `src/`
Contains reusable implementation:
- dataset builders
- model classes
- train/test logic
- utility functions

### `main.py`
Should only:
- load the composed Hydra config
- initialize W&B if requested
- dispatch to `train` or `test`

## W&B usage

When you run with:
```bash
python main.py logger=wandb
```

the template logs:
- the full resolved Hydra config
- model and dataset choices
- task information
- scalar metrics from `wandb.log(...)`

Use W&B to compare runs, not handwritten notes.
