# Research Template Docs

This documentation describes a **task-aware** project structure for research codebases that use:

- **Hydra** for configuration
- **Weights & Biases** for experiment tracking
- **task-oriented boundaries** for datasets, models, and loops

## Core idea

The project is organized around three extension points:

- **task**: owns the problem definition, training loop, evaluation logic, and batch contract
- **model**: owns the method used for that task
- **dataset**: owns the data source for that task

A practical rule:

- add a **new model** when the learning problem stays the same
- add a **new dataset** when the sample format stays compatible with the same task
- add a **new task** when the learning problem itself changes

## Where to start

Read these pages in order:

1. **Getting Started**
2. **Architecture**
3. **Use Cases**
4. **Zero-shot MNIST with CLIP**
