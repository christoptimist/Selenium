from typing import Dict, Any
import yaml
import logging

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load a YAML configuration file
    """
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        logging.error(f"Configuration file {config_path} not found")
        raise