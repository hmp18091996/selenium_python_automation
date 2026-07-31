from pages.inventory_page import InventoryPage

def test_inventory_title(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    assert inventory.get_title() == "Products"


def test_inventory_item_count(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    assert inventory.get_item_count() == 6


def test_add_to_cart(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"