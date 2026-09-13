from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME_FORM = (By.ID, "first-name")
    LAST_NAME_FORM = (By.ID, "last-name")
    POSTAL_CODE_FORM = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")
    TOTAL_COST = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME_FORM)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME_FORM)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.POSTAL_CODE_FORM)).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(
            self.BUTTON_CONTINUE)).click()

    def price_check(self, expected_cost):
        return self.wait.until(EC.text_to_be_present_in_element(
              self.TOTAL_COST, str(expected_cost)))
