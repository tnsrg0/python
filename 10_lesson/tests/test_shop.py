import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.store_home_page import StoreHomepage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Покупка товаров в интернет-магазине")
@allure.title("Сквозной сценарий покупки набора товаров")
@allure.description(
    "Тест проверяет авторизацию,"
    "добавление трех товаров в корзину,"
    "заполнение формы доставки и финальную стоимость"
    )
@allure.severity("critical")
def test_shop():
    with allure.step("Инициализация драйвера Firefox"):
        driver = webdriver.Firefox()
    login_page = LoginPage(driver, "https://saucedemo.com")
    login_page.open_login_page()
    with allure.step("Авторизация"):
        login_page.input_login_and_password('standard_user', 'secret_sauce')
        login_page.click_login()
    store_page = StoreHomepage(driver)
    with allure.step("Добавление товаров в корзину"):
        store_page.add_to_cart(store_page.SAUCE_LABS_BACKPACK)
        store_page.add_to_cart(store_page.SAUCE_LABS_BOLT_T_SHIRT)
        store_page.add_to_cart(store_page.SAUCE_LABS_ONESIE)
    with allure.step("Перейти в корзину"):
        store_page.go_to_cart()
    cart_page = CartPage(driver)
    with allure.step("Переход к оформлению покупки из корзины"):
        cart_page.press_checkout()
    checkout_page = CheckoutPage(driver)
    with allure.step("Заполнение контактных данных покупателя"):
        checkout_page.fill_form('Tanya', 'Pogozhnikova', '658252')
        checkout_page.click_continue()
    with allure.step(
        "Проверка, что итоговая стоимость заказа составляет 58.29"
    ):
        assert checkout_page.price_check('58.29')
    driver.quit()
