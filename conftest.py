# -*- coding: utf-8 -*-
import importlib
import jsonpickle
import pytest
import json
import os.path
from _pytest.runner import runtestprotocol
from fixture.application import Application
fixture = None
target = None


def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            print(item.name, report.outcome)
    return True


def load_config(file):
    global target
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file, encoding="utf-8") as f:
        target = json.load(f)
    return target


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None or not fixture.is_valid():
        browser = load_config(request.config.getoption("--browser"))["chrome"]
        web_config = load_config(request.config.getoption("--target"))["web"]
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.destroy()
        pass
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# Зацепки которые запускаются автоматически PyTest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="browser.json")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


# Генератор модулей загрузки тестовых данных
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.endswith("json"):
            n = fixture.find("json")
            file = fixture[:n] + "." + fixture[n:]
            file = file.replace("_", "/")
            testdata = load_from_json(file)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s" % file),  encoding="utf-8") as f:
        file = f.read()
        return jsonpickle.decode(file)
