from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    calc_page = CalculatorPage(
        driver,
        "https://bonigarcia.dev/selenium-webdriver-java"
        "/slow-calculator.html")
    calc_page.open_calculator_page()
    calc_page.delay_input(45)
    calc_page.click_button(calc_page.SEVEN)
    calc_page.click_button(calc_page.PLUS)
    calc_page.click_button(calc_page.EIGHT)
    calc_page.click_button(calc_page.EQUALS)
    assert calc_page.response_delay_check("15", timeout=50)
    driver.quit()
