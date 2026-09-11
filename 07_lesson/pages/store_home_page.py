from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StoreHomepage:

    SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SAUCE_LABS_BOLT_T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart(self, button_locator):
        self.wait.until(EC.element_to_be_clickable(
            button_locator)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            self.CART)).click()
