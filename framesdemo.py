from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.PARTIAL_LINK_TEXT, "Free Access to InterviewQues/Re").click()

openedwindow = driver.window_handles
driver.switch_to.window(openedwindow[1])
fulltext = driver.find_element(By.CSS_SELECTOR, ".red").text
var = fulltext.split("at")[1].strip().split(" ")[0]
driver.close()

driver.switch_to.window(openedwindow[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(var)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("test@123")
adminuserrdrp = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
adminuserrdrp.select_by_index(2)
driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
