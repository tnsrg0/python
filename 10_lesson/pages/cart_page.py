from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:

    BUTTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Перейти к оформлению заказа (нажать кнопку Checkout)")
    def press_checkout(self) -> None:
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_CHECKOUT)).click()
