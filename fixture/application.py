# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from helper.calculator_page_helper import CalculatorPageHelper
from log import log


class Application:

    def __init__(self, browser, base_url):
        log.debug(browser["name"])
        self.OS = sys.platform
        log.debug("OS: " + self.OS)
        if browser["name"] == "firefox":
            self.caps = DesiredCapabilities.FIREFOX
            self.caps["marionette"] = True
            # равнозначно указанию в переменной Path
            if self.OS not in ("dos", "win32", "win16"):
               self.caps["binary"] = browser["path_linux"]
               self.caps["acceptSslCerts"] = True
               profile = browser["profile_linux"]
            else:
               profile = browser["profile"]
            self.profile = webdriver.FirefoxProfile(profile)
            if self.OS not in ("dos", "win32", "win16"):
                self.profile.set_preference("print.always_print_silent", True)
                self.profile.set_preference("print.show_print_progress", False)
            self.profile.accept_untrusted_certs = True
            self.driver = webdriver.Firefox(firefox_profile=self.profile)
            log.debug(self.driver.capabilities['moz:processID'])
        elif browser["name"] == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--disable-print-preview')
            chrome_options.add_argument('--ignore-certificate-errors')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser["name"] == "ie":
            # Требуют подписки сертификата
            self.driver = webdriver.Ie(executable_path='IEDriverServer.exe')
        elif browser["name"] == "edge":
            self.driver = webdriver.Edge()
        elif browser["name"] == "opera":
            self.driver = webdriver.Opera()
        elif browser["name"] == "remote":
            capabilities = {
                "browserName": "chrome",
                "version": "68.0",
                #"screenResolution": "1280x1024x24",
                "enableVNC": True,
                "enableVideo": False,
            }
            self.driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                desired_capabilities=capabilities)
        else:
            raise ValueError("Unrecognized browser %s" % browser["name"])
        # self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.base_url = base_url
        log.debug(self.driver.base_url)
        self.calc = CalculatorPageHelper(self)
        self.driver.get(self.driver.base_url)
        #self.calc.wait_for_page_to_load(60)

    # Валидная ли сессия, открыт ли браузер
    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        log.debug("destroy browser")
        self.driver.quit()
