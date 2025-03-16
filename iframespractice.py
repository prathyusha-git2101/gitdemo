import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#Switching to frame
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Home").click()
textgiv = driver.find_element(By.CSS_SELECTOR, "div[id='salesEndHeader'] div[class='clearfix']").text
coupon = textgiv.split("coupon")[1].strip(" ").split(" ")[0]
print("your coupon code is ", coupon)
#aftergetting text moving back to default content
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed())
driver.find_element(By.ID, "hide-textbox").click()
print(driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed())
time.sleep(2)


