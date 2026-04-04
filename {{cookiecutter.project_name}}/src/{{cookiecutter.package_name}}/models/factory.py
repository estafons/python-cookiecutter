from omegaconf import DictConfig

from src.{{cookiecutter.package_name}}.models.backbones import load_backbone
from src.{{cookiecutter.package_name}}.models.baseline_classifier import BaselineClassifier
from src.{{cookiecutter.package_name}}.models.clip_linear_classifier import CLIPLinearClassifier


def build_model(cfg: DictConfig, num_classes: int, input_dim: int):
    if cfg.task.name != "classification":
        raise ValueError(f"Unsupported task for model factory: {cfg.task.name}")

    if cfg.model.builder == "baseline_classifier":
        return BaselineClassifier(
            input_dim=input_dim,
            hidden_dim=cfg.model.hidden_dim,
            num_classes=num_classes,
        )

    if cfg.model.builder == "clip_linear_classifier":
        backbone, feature_dim = load_backbone(
            backbone_type="clip",
            model_name=cfg.model.pretrained_model_name,
        )
        return CLIPLinearClassifier(
            backbone=backbone,
            feature_dim=feature_dim,
            num_classes=num_classes,
            freeze_backbone=cfg.model.freeze_backbone,
        )

    raise ValueError(f"Unsupported model builder: {cfg.model.builder}")
