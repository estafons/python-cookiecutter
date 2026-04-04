# Architecture

## Main assumption

This architecture assumes that a project grows around **tasks**.

A task owns:

- the sample contract
- the model output meaning
- the loss
- the metrics
- the outer train/test/eval logic

## What counts as a new task?

Create a new task when the **learning problem itself changes**.

Typical signals:

- the sample structure changes substantially
- the target type changes
- the model input/output meaning changes
- the problem-level evaluation logic changes

### Examples

- `item, label` → classification
- `item, target` → regression
- `item1, item2` → pairwise / matching
- `anchor, positive, negative` → metric learning

## What usually does NOT require a new task?

These are usually changes **within** a task:

- changing the loss
- changing metrics
- changing the optimizer
- changing the scheduler
- changing batch collation
- changing augmentation
- changing the backbone

So:
- CLIP classifier vs ResNet classifier is usually still **classification**
- cross-entropy vs focal loss is usually still **classification**

## Practical boundaries

### `main.py`
Only orchestration:
- load config
- initialize W&B
- dispatch to the selected task

### `tasks/`
Owns:
- train/test/eval loop
- loss selection
- metric computation
- assumptions about batch format

### `models/`
Owns:
- architecture
- forward contract required by the task

### `data/`
Owns:
- loading
- transforms
- normalization into the task's expected format
