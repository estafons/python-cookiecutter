import hydra
from omegaconf import DictConfig, OmegaConf
import wandb

from src.{{cookiecutter.package_name}}.train import train


@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

    run = None
    if "logger" in cfg and cfg.logger is not None:
        target = cfg.logger.get("_target_", None)
        if target == "wandb.init":
            logger_cfg = OmegaConf.to_container(cfg.logger, resolve=True)
            run = wandb.init(**logger_cfg)

    try:
        train(cfg)
    finally:
        if run is not None:
            run.finish()


if __name__ == "__main__":
    main()