# Zero-shot MNIST with CLIP

This page walks through a simple starting scenario:

> The project starts without a task defined yet, and you want to do **MNIST classification zero-shot with CLIP**.

For this example, the first task you add is **classification**.

## Why this is a new task at the start

At the beginning, the project has no task boundary yet.

MNIST zero-shot classification assumes:

- one image as input
- one class label as target
- classification-style evaluation

So the first task you define is:

- `classification`

---

## What to add

### 1. Add the task config

Create:

- `configs/task/classification.yaml`

Example:

```yaml
name: classification
label_field: label
input_field: image
```

### 2. Add the task logic

Create:

- `src/<package_name>/tasks/classification.py`

That file should own:

- how batches are read
- how logits or scores are produced
- how predictions are evaluated
- classification metrics such as accuracy

At minimum, implement:

- `run_classification(cfg)`

### 3. Add the dataset config

Create:

- `configs/data/mnist.yaml`

Example:

```yaml
name: mnist
task: classification
builder: mnist
num_classes: 10
class_names:
  - zero
  - one
  - two
  - three
  - four
  - five
  - six
  - seven
  - eight
  - nine
```

### 4. Add the dataset loader

Edit:

- `src/<package_name>/data/factory.py`

Add a `mnist` branch that returns classification-compatible samples.

A good normalized sample format is:

```python
{
    "image": image_tensor_or_pil,
    "label": int_label,
}
```

### 5. Add the model config

Create:

- `configs/model/clip_zeroshot_classifier.yaml`

Example:

```yaml
name: clip_zeroshot_classifier
builder: clip_zeroshot_classifier
pretrained_model_name: openai/clip-vit-base-patch32
prompt_template: "a photo of the digit {}"
```

### 6. Add the model implementation

Create:

- `src/<package_name>/models/clip_zeroshot_classifier.py`

This model should:

1. load pretrained CLIP
2. encode the candidate class prompts once
3. encode the input image
4. compute image-text similarity
5. return classification scores over the 10 class names

In other words, for zero-shot CLIP classification, the "classifier" is built from text prompts, not a trainable linear head.

### 7. Register the model

Edit:

- `src/<package_name>/models/factory.py`

Add a branch for `clip_zeroshot_classifier`.

### 8. Register the task dispatcher

Edit:

- `src/<package_name>/run.py`

Add a dispatch branch to call `run_classification(cfg)` when `cfg.task.name == "classification"`.

### 9. Add an experiment config

Create:

- `configs/experiment/mnist_clip_zeroshot.yaml`

Example:

```yaml
# @package _global_

defaults:
  - override /task: classification
  - override /model: clip_zeroshot_classifier
  - override /data: mnist

tags: ["mnist", "clip", "zeroshot", "classification"]
```

---

## What you do NOT need to change

Usually do not edit:

- `main.py`

Keep it as orchestration only.

---

## How to run it

```bash
python main.py experiment=mnist_clip_zeroshot logger=wandb
```

Because the template defaults to local/offline W&B mode, this will log locally unless you explicitly set:

```bash
WANDB_MODE=online
```

---

## Best practice for this example

The clean separation is:

- task = classification
- dataset = MNIST
- model = CLIP zero-shot classifier

That way, later you can add:

- another classification dataset
- another classification model
- another classification experiment

without rewriting the whole structure.
