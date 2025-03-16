import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

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
#sum validations
amounts=driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amt in amounts:
    sum = int(amt.text) + sum
totamt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totamt
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
discper = (driver.find_element(By.CSS_SELECTOR, ".discountPerc").text)
finalldiscper = int(discper.replace("%",""))
print(finalldiscper)
discamt = totamt * (finalldiscper/100)
discfinal = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totamt > discfinal
time.sleep(3)


