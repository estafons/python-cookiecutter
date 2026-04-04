# Getting Started

This page explains how to start from the template and make your first meaningful change.

## 1. Create the environment

```bash
conda env create -f environment.yaml
conda activate <your-project-name>
```

## 2. Install the package in editable mode

```bash
pip install -e .
```

## 3. Install git hooks

```bash
pre-commit install
```

## 4. (Optional) login to W&B

The template assumes **offline mode by default**. That means you can run locally without syncing to the cloud.

```bash
wandb login
```

## 5. Run the default configuration

```bash
python main.py
```

If the run starts and prints the Hydra config, the template is set up correctly.

---

## Recommended workflow

When working on the project, think in this order:

1. **What task am I solving?**
2. **What model do I want to use for that task?**
3. **What dataset do I want to run on?**
4. **Is this a one-off run or a named experiment?**

That gives you a stable habit:

- task logic goes in `src/<package>/tasks/`
- model logic goes in `src/<package>/models/`
- dataset logic goes in `src/<package>/data/`
- reproducible combinations go in `configs/experiment/`

---

## First real example

For a concrete walkthrough, read:

- **Zero-shot MNIST with CLIP**

That example assumes the project starts without a task defined yet, so the first thing you do is add a **classification task**.
