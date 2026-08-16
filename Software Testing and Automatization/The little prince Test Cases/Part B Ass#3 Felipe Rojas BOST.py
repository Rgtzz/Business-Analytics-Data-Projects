from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time

#Running the chrome on incognito mode due to problems with cookies and password manager.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)


#My code starts from here
#Open the Website
driver.get("https://www.saucedemo.com/")

time.sleep(3)

# Get into the Website
username_FR = driver.find_element(By.ID, "user-name")
password_FR = driver.find_element(By.ID, "password")
login_FR = driver.find_element(By.ID, "login-button")

time.sleep(2)

#Login
username_FR.send_keys("standard_user")
password_FR.send_keys("secret_sauce")
login_FR.click()

time.sleep(3)

#Add two products to the cart
product1_FR = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
product1_FR.click()

product2_FR = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
product2_FR.click()

time.sleep(3)


#Click the cart and then goes to the page for the checkout
cart_FR = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_FR.click()

time.sleep(4)

checkout_FR = driver.find_element(By.ID, "checkout")
checkout_FR.click()

time.sleep(3)

#Filling the form
first_name_FR = driver.find_element(By.ID, "first-name")
last_name_FR = driver.find_element(By.ID, "last-name")
postal_code_FR = driver.find_element(By.ID, "postal-code")
continue_FR = driver.find_element(By.ID, "continue")

time.sleep(2)

first_name_FR.send_keys("Felipe")
last_name_FR.send_keys("Rojas")
postal_code_FR.send_keys("12345")
continue_FR.click()

time.sleep(3)

#Finish the purchase
finish_FR = driver.find_element(By.XPATH, ("//*[@id='finish']"))
finish_FR.click()

time.sleep(3)

#Assertion to confirm that the purchase was completed
try:
    confirmation_message_FR = driver.find_element(By.CLASS_NAME, "complete-header")
    assert confirmation_message_FR.text == "THANK YOU FOR YOUR ORDER"
    print("Test Passed")
except (NoSuchElementException, AssertionError):
    print("Test Failed")
