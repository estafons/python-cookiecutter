# Add a Dataset

Add a new dataset when the **task stays the same** and the new data can be normalized to the same sample format.

## Create

- `configs/data/new_dataset.yaml`

## Edit

- `src/<package_name>/data/factory.py`

## Optional

- `src/<package_name>/data/new_dataset.py`

## Usually do not edit

- `main.py`
- task logic, unless the dataset changes the learning problem itself

## Checklist

1. Add a dataset config.
2. Implement loading and preprocessing.
3. Normalize the returned samples to the task format.
4. Register the dataset in the data factory.

## Example

If the classification task expects samples like:

```python
{"image": ..., "label": ...}
```

then every classification dataset should be normalized to that structure, even if the raw source data differs.
