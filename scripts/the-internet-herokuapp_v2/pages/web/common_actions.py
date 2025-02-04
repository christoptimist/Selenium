from pages.base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.helpers import _screenshot
from utilities.decorators import _retry_on_stale_element

class CommonActions(BasePage):
    @_retry_on_stale_element(max_retries=3)
    def _wait_element(self, driver, locator, logger, config, timeouts = None) -> tuple[By, str]:
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
            _screenshot(driver, logger)
            logger.error(f"Target element is not found {locator}")
            raise
    
    @_retry_on_stale_element(max_retries=3)
    def _enter_text_field(self, driver, locator, text, logger, config, timeouts = None) -> None:
        resolved_timeouts = (
            timeouts or (
                config.get("timeouts", {}).get("explicit_wait") if config else 10
            )
        )
        try:
            element = WebDriverWait(driver, resolved_timeouts).until(
                EC.visibility_of_element_located(locator)
            )

            element.click()
            element.send_keys(text)
        except Exception as e:
            _screenshot(driver, logger)
            logger.error(f"Target element is not found {locator}")
            raise

    @_retry_on_stale_element(max_retries=3)
    def _click_button(self, driver, locator, logger, config, timeouts = None) -> None:
        resolve_timeouts = (
            timeouts or (
                config.get("timeouts", {}).get("explicit_wait") if config else 10
            )
        )
        try:
            WebDriverWait(driver, resolve_timeouts).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except TimeoutException as e:
            logger.error(f"Target element is not found {locator}")
            raise