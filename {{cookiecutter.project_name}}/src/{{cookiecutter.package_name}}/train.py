from omegaconf import DictConfig
import wandb

from src.{{cookiecutter.package_name}}.data.factory import build_data
from src.{{cookiecutter.package_name}}.models.factory import build_model
from src.{{cookiecutter.package_name}}.utils.seed import set_seed


def train(cfg: DictConfig) -> None:
    set_seed(cfg.seed)

    data_bundle = build_data(cfg)
    model = build_model(cfg, num_classes=data_bundle["num_classes"], input_dim=data_bundle["input_dim"])

    print(f"Training {cfg.model.name} on {cfg.data.name}")
    print(f"Model: {model}")
    print(f"Train samples: {len(data_bundle['train_data'])}")
    print(f"Trainer config: {cfg.trainer}")

    if wandb.run is not None:
        wandb.log({
            "task": 0,
            "train/num_samples": len(data_bundle["train_data"]),
            "data/input_dim": data_bundle["input_dim"],
            "data/num_classes": data_bundle["num_classes"],
        })
