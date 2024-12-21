import yaml
import os


def load_config(config_name="config.yml", config_dir="./config"):
    file_path = os.path.join(config_dir, config_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")

    with open(file_path, "r") as file:
        return yaml.safe_load(file)