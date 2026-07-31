import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS", "true") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver.save_screenshot(f"screenshots/{request.node.name}.png")
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)