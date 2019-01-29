import inspect
from log import log


def name_test():
    for function_name in inspect.stack():
        if function_name[3][:5] == "test_":
            log.info(function_name[3])
            return function_name[3][5:]


def initializing(tests):
    def init_test_data(app, test_data):

        name_test()
        log.debug(test_data)
        # initializing
        app.calc.click_ac()

        tests(app, test_data)

    return init_test_data
