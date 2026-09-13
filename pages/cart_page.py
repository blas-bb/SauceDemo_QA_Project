from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")
    ITEM_NAMES = (By.CSS_SELECTOR, "div.inventory_item_name")
    CART_ITEMS = (By.CSS_SELECTOR, "div.cart_item")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def _remove_button(self, product_slug):
        return (By.ID, f"remove-{product_slug}")

    def get_title(self):
        return self.text(self.TITLE)

    def get_item_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [element.text for element in elements]

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_product(self, product_slug):
        self.click(self._remove_button(product_slug))

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def start_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
