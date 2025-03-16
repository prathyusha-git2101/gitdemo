import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@class= 'search-keyword']").send_keys("ber")
time.sleep(2)
products=driver.find_elements(By.XPATH, "//div[@class ='product']")
count = len(products)
assert count > 0
for product in products:
    product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)





time.sleep(3)


