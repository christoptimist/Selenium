import os
import yaml
import logging

def _load_config(file_path="config/dev.yaml"):
    """
    Load configuration from a YAML file
    :param file_path: Path to the YAML file
    :return: Dictionary
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logging.info(f"File not found: {file_path}")
        raise
    except yaml.YAMLError as e:
        logging.error(f"Error loading YAML file: {e}")
        raise