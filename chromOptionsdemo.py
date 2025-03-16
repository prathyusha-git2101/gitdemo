from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.get_screenshot_as_file("chromoptions.png")
print(driver.title)
