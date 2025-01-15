from web_browser.interfaces.i_web_driver_factory import IWebDriverFactory

class WebDriverManager(IWebDriverFactory):
    def __init__(self, driver_factory: IWebDriverFactory):
        self._driver_factory = driver_factory

    def create_driver(self):
        return self._driver_factory.create_driver()
    
    def quit_driver(self):
        return self._driver_factory.quit_driver()
    
    def find_element(self):
        return self._driver_factory.find_element()
    
    def execute_script(self):
        return self._driver_factory.execute_script()
    
    def webdriverwait(self):
        return self._driver_factory.wait()