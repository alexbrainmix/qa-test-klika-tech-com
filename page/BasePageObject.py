import inspect
import time
from selenium.webdriver.support.wait import WebDriverWait
from log import log


class BasePageObject(object):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.timeout_max = 10

    def wait_for_page_to_load(self, timeout = 60):
        WebDriverWait(self.driver, timeout).until(lambda s: self.driver.base_url in s.current_url)
        log.debug(inspect.stack()[0][3])
        return self

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            log.debug("not find_element: " + inspect.stack()[0][3] + str(locator))
        self.get_screenshot_as_file()
        return False

    def sleep(self, value):
        time.sleep(value)

    def get_screenshot_as_file(self):
        self.driver.get_screenshot_as_file(time.strftime('%Y-%m-%d %H-%M-%S') + ".png")
