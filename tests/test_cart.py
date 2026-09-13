BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


def test_add_one_product(logged_in, inventory_page):
    inventory_page.add_product(BACKPACK)
    assert inventory_page.get_cart_count() == 1


def test_add_two_products(logged_in, inventory_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.add_product(BIKE_LIGHT)
    assert inventory_page.get_cart_count() == 2


def test_product_is_visible_in_cart(logged_in, inventory_page, cart_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_remove_product_from_cart(logged_in, inventory_page, cart_page):
    inventory_page.add_product(BACKPACK)
    inventory_page.open_cart()
    cart_page.remove_product(BACKPACK)
    assert cart_page.get_item_count() == 0


def test_continue_shopping_returns_to_products(
    logged_in, inventory_page, cart_page
):
    inventory_page.open_cart()
    cart_page.continue_shopping()
    assert inventory_page.get_title() == "Products"
