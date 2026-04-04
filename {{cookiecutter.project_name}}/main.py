import hydra
from omegaconf import DictConfig, OmegaConf
import wandb

from src.{{cookiecutter.package_name}}.run import run


@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

    run_logger = None
    if "logger" in cfg and cfg.logger is not None:
        target = cfg.logger.get("_target_", None)
        if target == "wandb.init":
            logger_cfg = OmegaConf.to_container(cfg.logger, resolve=True)
            run_logger = wandb.init(**logger_cfg)
            wandb.config.update(
                OmegaConf.to_container(cfg, resolve=True),
                allow_val_change=True,
            )

    try:
        run(cfg)
    finally:
        if run_logger is not None:
            run_logger.finish()


if __name__ == "__main__":
    main()
