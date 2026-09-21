import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор с задержкой")
@allure.title("Проверка сложения двух чисел с заданной задержкой ответа")
@allure.description(
    "Тест проверяет корректность сложения 7 + 8 на калькуляторе с задержкой"
    )
@allure.severity("normal")
def test_calculator():
    with allure.step("Инициализация драйвера Chrome"):
        driver = webdriver.Chrome()
    calc_page = CalculatorPage(
        driver,
        "https://bonigarcia.dev/selenium-webdriver-java"
        "/slow-calculator.html"
    )
    calc_page.open_calculator_page()
    with allure.step("Ввод значения задержки"):
        calc_page.delay_input(45)
    with allure.step("Ввод выражения : 7 + 8 ="):
        calc_page.click_button(calc_page.SEVEN)
        calc_page.click_button(calc_page.PLUS)
        calc_page.click_button(calc_page.EIGHT)
        calc_page.click_button(calc_page.EQUALS)
    with allure.step("Проверка, что сумма равна 15, с заданной задержкой"):
        assert calc_page.response_delay_check("15", timeout=50)
    driver.quit()
