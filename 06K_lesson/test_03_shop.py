from selenium import webdriver
from selenium.webdriver.common.by import By


def test_calculator():
    driver = webdriver.FireFox()
    # 1. Откройте страницу
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    # 2. Авторизуйтесь как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # 3. Добавьте в корзину товары
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    # 4. Перейдите в корзину.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # 5. Нажмите Checkout.
    driver.find_element(By.ID, "checkout").click()
    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс.
    driver.find_element(By.ID, "first-name").send_keys("Tanya")
    driver.find_element(By.ID, "last-name").send_keys("Pogozhnikova")
    driver.find_element(By.ID, "postal-code").send_keys("658252")
    # 7. Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()
    # 8. Прочитайте со страницы итоговую стоимость (Total).
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    # 9. Закройте браузер.
    driver.quit()
    # 10. Проверьте, что итоговая сумма равна $58.29.
    assert "58.29" in total
