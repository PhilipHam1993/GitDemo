import pytest
import fixture
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
