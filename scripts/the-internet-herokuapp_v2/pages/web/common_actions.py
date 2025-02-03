from pages.base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from utitlities.helpers import _screenshot

class CommonActions(BasePage):
    def _wait_element(self, driver, locator, logger, config, timeouts = None):

        resolved_timeouts = (
            timeouts or (
                config.get("timeouts", {}).get("explicit_wait") if config else 10
            )
        )
        try:
            element = WebDriverWait(driver, resolved_timeouts).until(
                EC.visibility_of_element_located(locator)
            )
            return element.get_attribute('id')
        except TimeoutException as e:
            _screenshot(driver, logger)
            logger.error(f"Target element is not found {locator}")
            raise
        