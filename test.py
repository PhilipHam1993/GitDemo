import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)


driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
searchLine = driver.find_element(By.XPATH, '//input[@type="search"]').send_keys('Walnuts - 1/4 Kg')
driver.find_element(By.XPATH, '//div[@class="product-action"]/button').click()
driver.find_element(By.XPATH, '//a/img[@alt="Cart"]').click()






