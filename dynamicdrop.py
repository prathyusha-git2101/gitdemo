import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("D:\chrrome web\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(3)
assert (driver.find_element(By.ID,"autosuggest").get_attribute("value")) == "Indfddia"
