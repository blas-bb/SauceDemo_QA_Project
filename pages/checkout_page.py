import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    TITLE = (By.CSS_SELECTOR, "span.title")
    SUMMARY_ITEMS = (By.CSS_SELECTOR, "div.cart_item")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")

    def fill_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.type(self.FIRST_NAME, first_name)
        time.sleep(0.5)

        self.type(self.LAST_NAME, last_name)
        time.sleep(0.5)

        self.type(self.POSTAL_CODE, postal_code)
        time.sleep(0.5)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)

    def get_error_message(self):
        return self.text(self.ERROR_MESSAGE)

    def get_title(self):
        return self.text(self.TITLE)

    def get_summary_item_count(self):
        return len(
            self.driver.find_elements(*self.SUMMARY_ITEMS)
        )

    def get_complete_message(self):
        return self.text(self.COMPLETE_HEADER)