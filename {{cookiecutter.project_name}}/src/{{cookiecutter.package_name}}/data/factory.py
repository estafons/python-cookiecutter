from omegaconf import DictConfig


def build_data(cfg: DictConfig) -> dict:
    if cfg.task.name != "classification":
        raise ValueError(f"Unsupported task for data factory: {cfg.task.name}")

    if cfg.data.builder == "dataset_a":
        return {
            "train_data": [(i, i % cfg.data.num_classes) for i in range(100)],
            "test_data": [(i, i % cfg.data.num_classes) for i in range(20)],
            "num_classes": cfg.data.num_classes,
            "input_dim": cfg.data.input_dim,
        }

    if cfg.data.builder == "dataset_b":
        return {
            "train_data": [(i, i % cfg.data.num_classes) for i in range(200)],
            "test_data": [(i, i % cfg.data.num_classes) for i in range(40)],
            "num_classes": cfg.data.num_classes,
            "input_dim": cfg.data.input_dim,
        }

    raise ValueError(f"Unsupported dataset builder: {cfg.data.builder}")
