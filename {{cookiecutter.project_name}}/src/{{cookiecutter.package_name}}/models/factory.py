from omegaconf import DictConfig

from src.{{cookiecutter.package_name}}.models.baseline import BaselineModel
from src.{{cookiecutter.package_name}}.models.my_model import MyModel


def build_model(cfg: DictConfig, num_classes: int, input_dim: int):
    if cfg.model.builder == "baseline":
        return BaselineModel(
            input_dim=input_dim,
            hidden_dim=cfg.model.hidden_dim,
            num_classes=num_classes,
        )

    if cfg.model.builder == "my_model":
        return MyModel(
            input_dim=input_dim,
            hidden_dim=cfg.model.hidden_dim,
            num_classes=num_classes,
        )

    raise ValueError(f"Unsupported model builder: {cfg.model.builder}")
