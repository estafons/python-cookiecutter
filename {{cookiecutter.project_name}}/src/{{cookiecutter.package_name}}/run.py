from omegaconf import DictConfig

from src.{{cookiecutter.package_name}}.train import train
from src.{{cookiecutter.package_name}}.test import test


def run(cfg: DictConfig) -> None:
    if cfg.task == "train":
        train(cfg)
    elif cfg.task == "test":
        test(cfg)
    else:
        raise ValueError(f"Unsupported task: {cfg.task}")
