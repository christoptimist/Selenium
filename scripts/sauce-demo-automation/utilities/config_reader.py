import yaml

def _load_config(file_path="config/dev.yaml"):
    """
    Load configuration from a YAML file
    :param file_path: Path to the YAML file
    :return: Dictionary
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)