from pages.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utitlities.helpers import _screenshot
from utitlities.decorators import retry_on_stale_element

class CommonActions(BasePage):
    # def _wait_element(self, driver, locator, logger, config, timeouts = None) -> tuple[By, str]:
    def _wait_element(self, driver, locator, logger) -> tuple[By, str]:
        # resolved_timeouts = (
        #     timeouts or (
        #         config.get("timeouts", {}).get("explicit_wait") if config else 10
        #     )
        # )
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return locator
        except TimeoutException as e:
            _screenshot(driver, logger)
            logger.error(f"Target element is not found {locator}")
            raise
        
    # def _enter_text_field(self, driver, locator, text, logger, config, timeouts = None) -> None:
    def _enter_text_field(self, driver, locator, text, logger) -> None:
        # resolved_timeouts = (
        #     timeouts or (
        #         config.get("timeouts", {}).get("explicit_wait") if config else 10
        #     )
        # )
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).send_keys(text)
        except Exception as e:
            _screenshot(driver, logger)
            logger.error(f"Target element is not found {locator}")
            raise