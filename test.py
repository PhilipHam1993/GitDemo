import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(5)

driver.get('https://rozetka.com.ua/ua/')

searchString = driver.find_element(By.XPATH, '//input[@name="search"]').send_keys('Металошукач Minelab Excalibur II')
time.sleep(2)
findButton = driver.find_element(By.XPATH, '//button[@class="button button_color_green button_size_medium search-form__submit"]').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]')))

confirmButtonText = driver.find_element(By.XPATH, '//span[@class="ctp-label"]').text
print(confirmButtonText)

confirmButton = driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()






