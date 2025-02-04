from datetime import datetime
import yaml
import os

def _load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'configuration.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
    
def _screenshot(driver, logger) -> bool:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    screenshot_path = os.path.join(os.path.dirname(__file__), '..', 'screenshot/')
    os.makedirs(screenshot_path, exist_ok=True)
    filepath = os.path.join(screenshot_path, f"timeouts_{timestamp}.png")
    logger.info('Performing screenshot for debugging purposes.')
    return driver.save_screenshot(filepath)