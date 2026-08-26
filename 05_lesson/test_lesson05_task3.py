from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
# Откройте страницу https://httpbin.qa-territory.online/links/10.
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()
    sleep(2)
# Найдите все ссылки на странице (тег <a>).
    links = driver.find_elements(By.TAG_NAME, "a")
    count_links = len(links)
# Проверьте, что количество ссылок равно 9.
    assert count_links == 9
# Проверьте, что все ссылки отображаются на странице.
    for link in links:
        assert link.is_displayed()
# Проверьте, что текст первой ссылки содержит "1"
    link_1 = links[0].text
    assert link_1 == '1'
    driver.quit()
