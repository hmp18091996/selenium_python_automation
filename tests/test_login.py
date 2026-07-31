from pages.login_page import LoginPage


def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_login_wrong_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "wrong_password")
    error = login.get_error_message()
    assert "Epic sadface" in error

# def test_fail_screenshot(logged_in_driver):
#     assert "wrong_url" in logged_in_driver.current_url