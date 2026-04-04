from omegaconf import DictConfig
import wandb

from src.{{cookiecutter.package_name}}.data.factory import build_data
from src.{{cookiecutter.package_name}}.models.factory import build_model
from src.{{cookiecutter.package_name}}.utils.seed import set_seed


def run_classification(cfg: DictConfig) -> None:
    set_seed(cfg.seed)

    data_bundle = build_data(cfg)
    model = build_model(
        cfg,
        num_classes=data_bundle["num_classes"],
        input_dim=data_bundle["input_dim"],
    )

    if cfg.trainer.task_mode == "train":
        print(f"Training {cfg.model.name} on {cfg.data.name}")
        print(f"Train samples: {len(data_bundle['train_data'])}")
        if wandb.run is not None:
            wandb.log({
                "stage": 0,
                "train/num_samples": len(data_bundle["train_data"]),
                "data/num_classes": data_bundle["num_classes"],
            })
        return

    if cfg.trainer.task_mode == "test":
        print(f"Testing {cfg.model.name} on {cfg.data.name}")
        print(f"Test samples: {len(data_bundle['test_data'])}")
        print(f"Checkpoint path: {cfg.ckpt_path}")
        if wandb.run is not None:
            wandb.log({
                "stage": 1,
                "test/num_samples": len(data_bundle["test_data"]),
                "data/num_classes": data_bundle["num_classes"],
            })
        return

    raise ValueError(f"Unsupported trainer.task_mode: {cfg.trainer.task_mode}")
