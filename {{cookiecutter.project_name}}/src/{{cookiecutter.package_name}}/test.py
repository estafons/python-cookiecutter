from omegaconf import DictConfig
import wandb

from src.{{cookiecutter.package_name}}.data.factory import build_data
from src.{{cookiecutter.package_name}}.models.factory import build_model


def test(cfg: DictConfig) -> None:
    data_bundle = build_data(cfg)
    model = build_model(cfg, num_classes=data_bundle["num_classes"], input_dim=data_bundle["input_dim"])

    print(f"Testing {cfg.model.name} on {cfg.data.name}")
    print(f"Model: {model}")
    print(f"Test samples: {len(data_bundle['test_data'])}")
    print(f"Checkpoint path: {cfg.ckpt_path}")

    if wandb.run is not None:
        wandb.log({
            "task": 1,
            "test/num_samples": len(data_bundle["test_data"]),
            "data/input_dim": data_bundle["input_dim"],
            "data/num_classes": data_bundle["num_classes"],
        })
