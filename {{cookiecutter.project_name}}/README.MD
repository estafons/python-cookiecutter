# {{ cookiecutter.project_name }}

This repository provides a **clean, structured starting point for Python research projects**.

It is designed to help you:
- write clean, consistent code
- manage experiments in a reproducible way
- separate configuration from implementation
- scale from simple experiments to more complex pipelines

It includes configuration for:
- Ruff (linting)
- Black (formatting)
- isort (import sorting)
- pre-commit (automated checks before commits)
- GitHub Actions (CI linting)
- Hydra (configuration management)

👉 See the sections below for detailed usage and workflow guidance.

---

# ⚙️ Initial Setup

### 1. Create the environment

```bash
conda env create -f environment.yaml
```

### 2. Activate it

```bash
conda activate {{ cookiecutter.project_name }}
```

### 3. Install pre-commit hooks

```bash
pre-commit install
```

This ensures that every commit:
- is properly formatted
- passes lint checks
- follows project standards

---

# 🧭 How to Think About This Project

This is not just a Python project — it is a **framework for running experiments**.

The most important principle:

👉 **Separate code from configuration**

- Python files (`.py`) → define logic (models, training, utilities)
- Config files (`.yaml`) → define experiment settings

### Why this matters

- You can reproduce results easily
- You avoid rewriting code for every experiment
- You can track and compare experiments cleanly

---

# 🚀 First Run

Run the project with default settings:

```bash
python main.py
```

If this works, your environment is set up correctly.

---

# 🧪 Running Experiments with Hydra

This project uses **Hydra** to manage configurations.

Instead of editing code, you override parameters from the command line.

### Example: change a parameter

```bash
python main.py model.hidden_dim=256
```

### Multiple overrides

```bash
python main.py training.batch_size=128 model.hidden_dim=512
```

### Switch configurations

```bash
python main.py model=mlp training=default
```

---

# 📁 Configuration Structure

```
configs/
├── config.yaml        # Entry point
├── model/             # Model configs
│   └── mlp.yaml
├── training/          # Training configs
│   └── default.yaml
```

### What each file does

- `config.yaml` → defines which configs are used
- `model/` → model architecture parameters
- `training/` → training hyperparameters

---

# 🧠 How to Work Properly (Important)

### ✅ Add new models via configs

Create:

```
configs/model/my_model.yaml
```

Run:

```bash
python main.py model=my_model
```

---

### ✅ Run experiments without editing code

```bash
python main.py model.hidden_dim=1024 training.batch_size=256
```

---

### ✅ Keep experiments reproducible

Hydra creates output folders automatically:

```
outputs/YYYY-MM-DD/HH-MM-SS/
```

These include:
- full config used
- logs
- outputs

---

# 🧹 Code Quality Tools

This project enforces clean and consistent code using the following tools.

---

## Ruff (linting)

```bash
ruff check --select=E,T201 .
ruff check --select=ALL .
```

Fix issues automatically:

```bash
ruff check . --fix
```

---

## isort (imports)

```bash
isort .
```

---

## Black (formatting)

```bash
black .
```

Preview changes:

```bash
black . --diff
```

---

## pre-commit

Install hooks:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

Skip hooks (not recommended):

```bash
git commit -m "message" --no-verify
```

---

# ⚠️ Common Mistakes

❌ Editing Python code for experiments  
→ Use Hydra overrides instead  

❌ Hardcoding parameters  
→ Move them to configs  

❌ Ignoring lint errors  
→ They often indicate real issues  

❌ Not tracking configurations  
→ Makes results impossible to reproduce  

---

# 🧩 Extending the Project

As your work grows, consider adding:

- `configs/data/` → dataset configs  
- `configs/logger/` → experiment tracking (e.g. W&B)  
- `configs/experiment/` → named experiment presets  

---

# 📚 References

- Ruff: https://docs.astral.sh/ruff  
- Black: https://github.com/psf/black  
- isort: https://pycqa.github.io/isort/  
- pre-commit: https://pre-commit.com/  
- Hydra: https://hydra.cc  

---

# 🧠 Final Advice

Treat this repository as:

> A system for running controlled, reproducible experiments — not just a codebase.

If used correctly, it will help you:
- keep your research organized
- reproduce results reliably
- scale experiments efficiently