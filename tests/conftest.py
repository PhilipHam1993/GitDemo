import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "EI":
        driver = webdriver.Edge()

    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
