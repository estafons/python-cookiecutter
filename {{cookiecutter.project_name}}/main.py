import hydra
from omegaconf import DictConfig

@hydra.main(config_path="configs", config_name="config")
def main(cfg: DictConfig):
    print(cfg.pretty())

if __name__ == "__main__":
    main()
