from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Dict, Any, Optional
import logging

class BasePage(ABC):
    @abstractmethod
    def _wait_element(self, driver: WebDriver, locator: tuple[By, str], logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> tuple[By, str]:
        pass