from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "span.title")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "div.inventory_item_name")
    SORT_SELECT = (By.CSS_SELECTOR, "select.product_sort_container")

    def _add_button(self, product_slug):
        return (By.ID, f"add-to-cart-{product_slug}")

    def _remove_button(self, product_slug):
        return (By.ID, f"remove-{product_slug}")

    def get_title(self):
        return self.text(self.TITLE)

    def add_product(self, product_slug):
        self.click(self._add_button(product_slug))

    def remove_product(self, product_slug):
        self.click(self._remove_button(product_slug))

    def open_cart(self):
        self.click(self.CART_LINK)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def get_product_names(self):
        return self.texts(self.PRODUCT_NAMES)

    def sort_by(self, value):
        select = Select(self.wait.until(EC.element_to_be_clickable(self.SORT_SELECT)))
        select.select_by_value(value)
