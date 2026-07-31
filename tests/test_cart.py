from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart_and_verify(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    cart = CartPage(logged_in_driver)

    # Add item to cart
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"

    # Open cart
    cart.open_cart()
    assert cart.get_cart_item_count() == 1

def test_checkout_button(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    cart = CartPage(logged_in_driver)

    inventory.add_first_item_to_cart()
    cart.open_cart()
    cart.click_checkout()

    assert "checkout-step-one" in logged_in_driver.current_url