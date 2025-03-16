import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
name = "prathyusha"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()
time.sleep(1)
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
confirmbut = driver.switch_to.alert
confirmbut.dismiss()

time.sleep(2)
