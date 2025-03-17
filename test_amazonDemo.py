import json
import os
import sys
from pageObjects.loginPage import LoginPage
from pageObjects.amazonhomepage import Homepage

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import browser_Instance

test_file_path = "C:\\Users\\raghu\\PycharmProjects\\amazonproject\\data\\test_item.json"
with open(test_file_path) as f:
    test_data = json.load(f)
    test_item123 = test_data["data"]


@pytest.mark.amazondata
@pytest.mark.parametrize("test_item", test_item123)
def test_demo(browser_Instance, test_item):
    driver = browser_Instance
    loginpage = LoginPage(driver)
    amazonhpobj = loginpage.loginpage(test_item["websitename"])
    amazonhpobj.homepage(test_item["product"])

