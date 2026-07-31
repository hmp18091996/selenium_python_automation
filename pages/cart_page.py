from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()


    def get_cart_item_count(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEMS))
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView();", btn)
        btn.click()
        self.wait.until(EC.url_contains("checkout"))