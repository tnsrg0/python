from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:

    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self) -> None:
        self.driver.get(self.url)
        self.driver.save_screenshot("screenshots/page-opened.png")

    @allure.step("Ввести учетные данные пользователя: {username}")
    def input_login_and_password(self, username: str, password: str) -> None:
        self.wait.until(EC.visibility_of_element_located(
            self.USER_NAME_INPUT)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(
            self.PASSWORD_INPUT)).send_keys(password)

    @allure.step("Нажать кнопку Войти (Login)")
    def click_login(self) -> None:
        self.wait.until(EC.element_to_be_clickable(
            self.LOGIN_BUTTON)).click()
