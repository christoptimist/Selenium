from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def _enter_text(driver, locator, text, logger):
    """
    Enter text into a text field
    :param locator: Tuple (By, Locator)
    :param text: Text to enter
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(text)
    except TimeoutException as e:
        logger.error(f"Element not found: {e}")

def _click_element(driver, locator, logger):
    """
    Click an element
    :param locator: Tuple (By, Locator)
    """
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    except TimeoutException as e:
        logger.error(f"Element not found: {e}")