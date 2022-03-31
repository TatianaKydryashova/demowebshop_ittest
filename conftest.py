import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action="store_true", help="Run driver in headless mode.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    browser = None
    if browser_name == "chrome":
        if not headless:
            browser = webdriver.Chrome()
        else:
            options = Options()
            options.add_argument("--headless")
            browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        if not headless:
            browser = webdriver.Firefox()
        else:
            options = Options()
            options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
