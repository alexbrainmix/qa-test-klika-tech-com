import pytest
import helper.helper as hh


symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]


def init(app):
    app.calc.click_ac()


@pytest.mark.parametrize("symbol", symbols)
def test_ac(app, symbol):
    init(app)
    app.calc.click_symbol(symbol)
    assert app.calc.get_display_text() == symbol
    app.calc.click_ac()
    assert app.calc.get_display_text() == ""


def test_maximum_digit_capacity(app):
    init(app)
    symbol = "9"
    max_number_str = ""
    while app.calc.get_display_text() == max_number_str:
        app.calc.click_symbol(symbol)
        max_number_str += symbol
    assert app.calc.get_display_text() == max_number_str


@hh.initializing
def enter_symbols(app, test_data):
    for c in test_data.expression:
        app.calc.click_symbol(c)


def test_calc(app, calc_calcjson):
    test_data = calc_calcjson
    enter_symbols(app, test_data)
    assert app.calc.get_display_text() == test_data.result
