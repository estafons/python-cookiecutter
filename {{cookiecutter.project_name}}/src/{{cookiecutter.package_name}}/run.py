from omegaconf import DictConfig

from src.{{cookiecutter.package_name}}.tasks.classification import run_classification


def run(cfg: DictConfig) -> None:
    if cfg.task.name == "classification":
        run_classification(cfg)
    else:
        raise ValueError(f"Unsupported task: {cfg.task.name}")
