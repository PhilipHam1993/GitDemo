from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome()

driver.get('https://rozetka.com.ua/ua/')




