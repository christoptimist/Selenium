from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Dict, Any, Optional
import logging

class BasePage(ABC):
    @abstractmethod
    def _wait_element(self, driver: WebDriver, locator: tuple[By, str], logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> tuple[By, str]:
        pass

    @abstractmethod
    def _enter_text_field(self, driver: WebDriver, locator: tuple[By, str], text: str, logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> None:
        pass

    @abstractmethod
    def _click_button(self, driver: WebDriver, locator: tuple[By, str], logger: logging.Logger, config: Optional[Dict[str, Any]], timeouts: Optional[int] = None) -> None:
        pass
