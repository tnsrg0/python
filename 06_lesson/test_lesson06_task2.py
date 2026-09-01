from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
# Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")
    driver.maximize_window()
# Установите cookie пользователя 1.
    driver.add_cookie({
       "name": "SESSION",
       "value": "YzJmOGRjMmEtMzk1Ny00ZDBkLWFkMDUtNmM3NDdlNzVlM2Uy",
       "domain": "gitflic.ru"
    })
# Обновите страницу.
    driver.refresh()
# Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/tnsrg")
# Сохраните текущий URL.
    url_user_1 = driver.current_url
# Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
# Установите cookie пользователя 2.
    driver.add_cookie({
       "name": "SESSION",
       "value": "NjZiM2IzMmQtYzQ2Mi00NTM0LWJlYzgtYjE1ZWNlNmE2YThk",
       "domain": "gitflic.ru"
    })
# Обновите страницу.
    driver.refresh()
# Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/qwasd_1")
# Сохраните текущий URL.
    url_user_2 = driver.current_url
# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user_1 != url_user_2
    driver.quit()
