from omegaconf import DictConfig


def build_model(cfg: DictConfig, num_classes: int, input_dim: int):
    """
    Build task-compatible models.

    This starter template intentionally does not ship with concrete models.
    Follow the docs to add your first model and register it here.
    """
    if cfg.task.name == "classification":
        raise NotImplementedError(
            "No classification model is registered yet. "
            "Add one in src/<package>/models/, create its config in configs/model/, "
            "and register it in build_model()."
        )

    raise ValueError(f"Unsupported task for model factory: {cfg.task.name}")