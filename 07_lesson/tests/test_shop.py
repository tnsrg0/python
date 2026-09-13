from selenium import webdriver
from pages.login_page import LoginPage
from pages.store_home_page import StoreHomepage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    login_page = LoginPage(
        driver, "https://www.saucedemo.com")
    login_page.open_login_page()
    login_page.input_login_and_password('standard_user', 'secret_sauce')
    login_page.click_login()
    store_page = StoreHomepage(driver)
    store_page.add_to_cart(store_page.SAUCE_LABS_BACKPACK)
    store_page.add_to_cart(store_page.SAUCE_LABS_BOLT_T_SHIRT)
    store_page.add_to_cart(store_page.SAUCE_LABS_ONESIE)
    store_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.press_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form('Tanya', 'Pogozhnikova', '658252')
    checkout_page.click_continue()
    assert checkout_page.price_check('58.29')
    driver.quit()
