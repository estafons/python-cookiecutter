# Add a Model

Add a new model when the **task stays the same** but the method changes.

## Create

- `configs/model/new_model.yaml`
- `src/<package_name>/models/new_model.py`

## Edit

- `src/<package_name>/models/factory.py`

## Usually do not edit

- `main.py`
- `src/<package_name>/tasks/*.py`

## Checklist

1. Add a Hydra config for the model.
2. Implement the model class.
3. Register the model in the model factory.
4. Make sure the model matches the task's expected output contract.

## Example

For classification, the task usually expects something like:

```python
logits = model(inputs)
```

So any new classification model should return logits with the expected shape.
