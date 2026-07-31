from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com")
print(driver.title)

# ❌ không dùng POM — code lộn xộn
def test_login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_login_wrong_password():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")  # lặp lại
    driver.find_element(By.ID, "password").send_keys("wrong")           # lặp lại
    driver.find_element(By.ID, "login-button").click()                  # lặp lại


# driver.quit()