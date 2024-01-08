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
addButton = driver.find_element(By.XPATH, '//div[@class="product-action"]/button')
addButton.click()
pocketButton = driver.find_element(By.XPATH, '//a/img[@alt="Cart"]')
pocketButton.click()
productNamePacket = driver.find_element(By.XPATH, '//div/p[@class="product-name"]')

assert 'Walnuts - 1/4 Kg' in productNamePacket.text
print(productNamePacket.text)

checkoutButton = driver.find_element(By.XPATH, '//div[@class="cart-preview active"]/div/button[@type="button"]')
checkoutButton.click()
time.sleep(3)
total = driver.find_element(By.XPATH, '//div/table/tbody/tr/td[5]/p')
assert '170' in total.text
print(total.text)













