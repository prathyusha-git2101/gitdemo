import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT,"Flight Booking").click()
openedwindows = driver.window_handles
driver.switch_to.window(openedwindows[1])
driver.find_element(By.CSS_SELECTOR,"#ctl00_mainContent_ddl_originStation1_CTXT").send_keys("be")
allelements = driver.find_elements(By.CSS_SELECTOR,".dropdownDiv ul li ")
for ele in allelements:
    if driver.find_element(By.CSS_SELECTOR, " a[value = 'BLR']").click():
        break

time.sleep(5)