# Add a Task

Add a new task when the **learning problem itself changes**, not just implementation details.

## Create a new task when

- the **sample structure** changes significantly
- the **target type** changes
- the **model input/output meaning** changes
- the **problem-level evaluation logic** changes

## Examples

- `item, label` → classification
- `item, target` → regression
- `item1, item2` → pairwise / similarity learning

## Usually NOT a new task

Do **not** create a new task just because you changed:

- loss function
- metrics
- optimizer or training settings
- batch collation

Those are usually variations **within** the same task.

---

## Create

- `configs/task/regression.yaml`
- `src/<package_name>/tasks/regression.py`

## Add task-specific models

- `configs/model/*_regressor.yaml`
- `src/<package_name>/models/*.py`

## Add task-compatible datasets

- `configs/data/<regression_dataset>.yaml`

## Edit

- `src/<package_name>/run.py`
- possibly `src/<package_name>/data/factory.py`
- possibly `src/<package_name>/models/factory.py`

## Usually do not edit

- `main.py`

## Best practice

Treat the task as the owner of:

- loss
- metrics
- loop structure
- assumptions about batch format
