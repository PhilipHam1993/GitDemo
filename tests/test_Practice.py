import time

import pytest
import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_practice(self):

        searchLine = self.driver.find_element(By.XPATH, '//input[@type="search"]')
        searchLine.send_keys('Walnuts - 1/4 Kg')
        time.sleep(3)
        addButton = self.driver.find_element(By.XPATH, '//div[@class="product-action"]/button')
        addButton.click()
        pocketButton = self.driver.find_element(By.XPATH, '//a/img[@alt="Cart"]')
        pocketButton.click()
        productNamePacket = self.driver.find_element(By.XPATH, '//div/p[@class="product-name"]')

        assert 'Walnuts - 1/4 Kg' in productNamePacket.text
        print(productNamePacket.text)

        checkoutButton = self.driver.find_element(By.XPATH, '//div[@class="cart-preview active"]/div/button[@type="button"]')
        checkoutButton.click()
        time.sleep(3)
        total = self.driver.find_element(By.XPATH, '//div/table/tbody/tr/td[5]/p')
        assert '170' in total.text
        print(total.text)
        orderButton = self.driver.find_element(By.XPATH, '//div/button[text()="Place Order"]')
        orderButton.click()

        countryForm = self.driver.find_element(By.XPATH, '//div/select')
        countryForm.click()
        countryOption = self.driver.find_element(By.XPATH, '//div/select/option')
        time.sleep(3)
        country = self.driver.find_element(By.XPATH, '//div/select/option[2]')
        country.click()
        assert 'Afghanistan' in country.text
        print(country.text)

        termAndUseButton = self.driver.find_element(By.XPATH, '//input[@type="checkbox"]')
        termAndUseButton.click()
        proceedButton = self.driver.find_element(By.XPATH, '//button')
        proceedButton.click()

