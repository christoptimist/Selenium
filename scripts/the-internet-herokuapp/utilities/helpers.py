from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from functools import wraps
from typing import Optional, Dict, Any
import logging

def retry_on_stale_element(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = kwargs.get("logger", None) or args[2] if len(args) > 2 else logging.getLogger(__name__)
            """
            Retry the function if a StaleElementReferenceException is raised
            """
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException:
                    logger.error(f"Stale element reference exception on attempt {attempt + 1}")
                    if attempt == max_retries - 1:
                        logger.error("Max retries reached, raising exception")
                        raise
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry_on_stale_element(max_retries=3)
def _wait_element(driver: WebDriver, locator: tuple[By, str], logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> WebElement:
    """
    Wait for an element to be visible
    """
    resolved_timeouts = (
        timeouts or (
            config.get("timeouts", {}).get("explicit_wait") if config else 10
        )
    )
    try:
        WebDriverWait(driver, resolved_timeouts).until(
            EC.visibility_of_element_located(locator)
        )
        return locator
    except TimeoutException as e:
        driver.save_screenshot("element_not_interactable.png")
        logger.error(f"Target element {locator} not interactable")
        raise

@retry_on_stale_element(max_retries=3)
def _enter_text_field(driver: WebDriver, locator: tuple[By, str], text: str, logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> WebElement:
    """
    Enter text into a text field
    """
    resolved_timeouts = (
        timeouts or (
            config.get("timeouts", {}).get("explicit") if config else 10
        )
    )
    try:
        return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator)
        ).send_keys(text)
    except TimeoutException as e:
        driver.save_screenshot("text_field_not_interactable.png")
        logger.error(f"Text field {locator} not interactable")
        raise

@retry_on_stale_element(max_retries=3)
def _click_button(driver: WebDriver, locator: tuple[By, str], logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> WebElement:
    """
    Click a button
    """
    resolved_timeouts = (
        timeouts or (
            config.get("timeouts", {}).get("explicit") if config else 10
        )
    )
    try:
       return WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
    except TimeoutException as e:
        driver.save_screenshot("button_not_interactable.png")
        logger.error(f"button element {locator} not interactable")
        raise