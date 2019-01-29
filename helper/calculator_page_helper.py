from page.calculator_page import CalculatorPage
from page.BasePageObject import BasePageObject


class CalculatorPageHelper(CalculatorPage, BasePageObject):

    def __init__(self, app):
        CalculatorPage.__init__(self)
        BasePageObject.__init__(self, app)

    def click_symbol(self, symbol):
        self.find_element(self.get_locator(symbol)).click()

    def click_ac(self):
        return self.find_element(self._ac).click()

    def get_display_text(self):
        return self.find_element(self._display).text
