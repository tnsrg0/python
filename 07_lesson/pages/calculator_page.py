from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY = (By.ID, "delay")
    SEVEN = (By.XPATH, "//span[text()='7']")
    PLUS = (By.XPATH, "//span[text()='+']")
    EIGHT = (By.XPATH, "//span[text()='8']")
    EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open_calculator_page(self):
        self.driver.get(self.url)
        self.driver.save_screenshot("screenshots/full_page.png")

    def delay_input(self, delay_value):
        delay_input_field = self.wait.until(EC.element_to_be_clickable(
            self.DELAY))
        delay_input_field.clear()
        delay_input_field.send_keys(str(delay_value))

    def click_button(self, button_locator):
        self.wait.until(EC.element_to_be_clickable(button_locator)).click()

    def response_delay_check(self, expected_value, timeout=50):
        separate_wait = WebDriverWait(self.driver, timeout)
        return separate_wait.until(EC.text_to_be_present_in_element(
            self.RESULT, str(expected_value)))
