import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


file_path = "C:\\Users\\raghu\\Downloads"

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.implicitly_wait(10)
driver.find_element(By.ID, "downloadButton").click()
#edit the excel with updated value

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)
print("edit completed")
#explicit wait
wait = WebDriverWait(driver,5)
toast_locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
price_column = driver.find_element(By.XPATH, "//div[text()='price')").get_attribute()