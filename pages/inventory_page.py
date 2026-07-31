from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:

    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def get_item_count(self):
        self.wait.until(EC.presence_of_element_located(self.ITEMS))
        return len(self.driver.find_elements(*self.ITEMS))

    def add_first_item_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()

    def get_cart_count(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text