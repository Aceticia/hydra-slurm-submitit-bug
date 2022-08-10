import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="./configs/", config_name="top")
def my_app(cfg: DictConfig) -> None:
    # add lines printing the config for diagnostic purposes:
    print("\n JOB CONFIG:")
    print(OmegaConf.to_yaml(cfg))  # print the job config
    from hydra.core.hydra_config import HydraConfig
    print("\n HYDRA CONFIG:")
    print(OmegaConf.to_yaml(HydraConfig.get()))  # print the Hydra config

if __name__ == "__main__":
    my_app()
