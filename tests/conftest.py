import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
