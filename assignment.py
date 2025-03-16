#print same like below given list
#send a list and compare the list with actual result ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
explist = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actlist = []
#class="product-name"
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
    actlist.append(product.find_element(By.CSS_SELECTOR, ".product-name").text)
    product.find_element(By.XPATH, "div/button").click()
print(actlist)
assert explist == actlist
driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#sum validations
amounts=driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for amt in amounts:
    sum = int(amt.text) + sum
totamt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totamt
#discamt = totamt * (discper/100)

#assert totamt < discfinal
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
discper = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
discval = int(discper.replace('%',""))
expdisc = totamt - ((totamt*discval)/100)
print(expdisc)
discfinal = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totamt > discfinal
assert  expdisc == discfinal





time.sleep(3)


