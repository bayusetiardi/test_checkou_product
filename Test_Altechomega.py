from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Test_belanja(unittest.TestCase):
    def setUp(self):
       self.browser = webdriver.Chrome()
    
    def test_1(self):
        browser=self.browser
        browser.get("https:/www.saucedemo.com/")
        browser.find_element(By.ID, value="user-name").send_keys("standard_user")
        browser.find_element(By.ID, value="password").send_keys("secret_sauce")
        browser.find_element(By.ID, value="login-button").click()
        time.sleep(3)
        
# validasi login sukses
        response_data = browser.find_element(By.CSS_SELECTOR,".title").text
        self.assertIn('Products', response_data)

#mencari product
        browser.find_element(By.CSS_SELECTOR, value="#item_4_title_link > div:nth-child(1)").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, value="#add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, value=".shopping_cart_link").click()
        time.sleep(1)

#validasi product in chart
        response_data = browser.find_element(By.CSS_SELECTOR,".inventory_item_name").text
        response_message = browser.find_element(By.CSS_SELECTOR,".title").text
        self.assertIn('Sauce Labs Backpack', response_data)
        self.assertEqual(response_message,'Your Cart')
        time.sleep(1)

#checkout
        browser.find_element(By.ID, value="checkout").click()
        time.sleep(1)

#Fill ID
        browser.find_element(By.ID, value="first-name").send_keys("Bayu")
        browser.find_element(By.ID, value="last-name").send_keys("Setiardi")
        browser.find_element(By.ID, value="postal-code").send_keys("55123")
        time.sleep(1)

        browser.find_element(By.ID, value="continue").click()

 #validasi product in checkout
        response_data = browser.find_element(By.CSS_SELECTOR,".inventory_item_name").text
        response_message = browser.find_element(By.CSS_SELECTOR,".title").text
        self.assertIn('Sauce Labs Backpack', response_data)
        self.assertEqual(response_message,'Checkout: Overview')
        time.sleep(3)

        browser.find_element(By.ID, value="finish").click()

        time.sleep(5)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()


