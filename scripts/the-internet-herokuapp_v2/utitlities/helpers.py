import yaml
import os

def _load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'configuration.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)