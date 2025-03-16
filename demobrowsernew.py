import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("D:\chrrome web\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("prathyusha")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("manu@123")
driver.find_element(By.ID,"exampleCheck1").click()
#css- //tag[name='name'---#id also turn out as css,.classname will turn out to css
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("prathyusha")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
#select for static dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_index(1)
#xpath- //html tag[@locator='name']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("sample text")
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()






time.sleep(15)

