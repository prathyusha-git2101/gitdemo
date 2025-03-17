import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser handling"
    )


@pytest.fixture(scope="function")
def browser_Instance(request):
    global driver
    browser_name = request.config.getoption("browser_name").lower()
    if browser_name == "chrome":

        chrome_driver_path = "D:\\chrome-web\\chromedriver-win32\\chromedriver.exe"
        chrome_options = ChromeOptions()
        chrome_service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    elif browser_name == "firefox":
        firefox_driver_path = "D:\\firefox-web\\geckodriver.exe"
        firefox_options = FirefoxOptions()
        firefox_service = FirefoxService(firefox_driver_path)
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    driver.implicitly_wait(5)
    driver.get("https://google.com")

    yield driver  # Provide driver instance to tests

    driver.quit()  # Cleanup after test execution


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
