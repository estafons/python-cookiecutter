from omegaconf import DictConfig


def build_data(cfg: DictConfig) -> dict:
    """
    Build task-compatible data objects.

    This starter template intentionally does not ship with concrete datasets.
    Follow the docs to add your first dataset and register it here.
    """
    if cfg.task.name == "classification":
        raise NotImplementedError(
            "No classification dataset is registered yet. "
            "Add one in src/<package>/data/, create its config in configs/data/, "
            "and register it in build_data()."
        )

    raise ValueError(f"Unsupported task for data factory: {cfg.task.name}")