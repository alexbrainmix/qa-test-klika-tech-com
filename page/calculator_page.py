from selenium.webdriver.common.by import By


class CalculatorPage(object):

    _display = (By.XPATH, "//div[@id='display']")
    _symbol = "//li[contains(text(), \'{}\')]"
    _ac = (By.XPATH, "//li[text()='AC']")

    def get_locator(self, symbol):
        return (By.XPATH, self._symbol.format(symbol))
