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
time.sleep(3)
addButton = driver.find_element(By.XPATH, '//div[@class="product-action"]/button').click()
pocketButton = driver.find_element(By.XPATH, '//a/img[@alt="Cart"]').click()
productNamePacket = driver.find_element(By.XPATH, '//div/p[@class="product-name"]').text
assert 'Walnuts - 1/4 Kg' in productNamePacket
 # time.sleep(5)
click = driver.find_element(By.XPATH, '//div/a[@class="increment"]').click()
clickTwo = driver.find_element(By.XPATH, '//div/a[@class="increment"]').click()
addButton = driver.find_element(By.XPATH, '//div[@class="product-action"]/button').click()
pocketButton = driver.find_element(By.XPATH, '//a/img[@alt="Cart"]').click()
productNamePacket = driver.find_element(By.XPATH, '//div/p[@class="product-name"]').text
assert 'Walnuts - 1/4 Kg' in productNamePacket

# driver.find_element(By.XPATH, '//div/div[4]/div/button[@type="button"]').click()
# driver.find_element(By.XPATH, '//ul/li/a[@class="product-remove"]').click()








