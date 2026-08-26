from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
# Откройте страницу https://httpbin.qa-territory.online.
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()
    sleep(2)
# Найдите и кликните на ссылку HTML Form.
    driver.find_element(
        By.LINK_TEXT, "HTML Form").click()
    sleep(2)
# Проверьте, что URL изменился на /forms/post.
    assert driver.current_url == \
        "https://httpbin.qa-territory.online/forms/post"
# Вернитесь назад на главную страницу.
    driver.back()
    sleep(2)
# Проверьте, что вернулись на исходный URL.
    assert driver.current_url == \
        "https://httpbin.qa-territory.online/"
    driver.quit()
