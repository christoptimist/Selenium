from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class ServiceConfiguration:
    def __init__(self):
        self.service = Service(executable_path=ChromeDriverManager().install())

    def get_service_configuration(self):
        return self.service