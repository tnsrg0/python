from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
# Откройте страницу https://httpbin.qa-territory.online/forms/post.
    driver.get("https://httpbin.qa-territory.online/forms/post")
    driver.maximize_window()
    sleep(2)
# Найдите поле ввода с названием custname.
    driver.find_element(By.NAME, "custname").click()
# Введите в него ваше имя Tanya.
    driver.find_element(By.NAME, "custname").send_keys("Tanya")
    sleep(2)
# Найдите кнопку Submit и нажмите на нее.
    driver.find_element(By.XPATH, "//*[text()='Submit order']").click()
    sleep(3)
# Проверьте, что после нажатия URL изменился.
    assert driver.current_url == "https://httpbin.qa-territory.online/post"
    driver.quit()
