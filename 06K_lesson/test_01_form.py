from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_filling_out_form():
    driver = webdriver.Edge()
    # 1. Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    driver.maximize_window()
    # 2. Заполните форму значениями
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    # 3. Нажмите кнопку Submit.
    submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    driver.execute_script("arguments[0].click();", submit)
    # 4. Проверьте (assert), что поле Zip code подсвечено красным.
    zip_code = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    element_classes = zip_code.get_attribute("class")
    assert "alert-danger" in element_classes
    # 5. Проверьте (assert), что остальные поля подсвечены зеленым.
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    assert "alert-success" in first_name.get_attribute("class")
    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "last-name"))
    )
    assert "alert-success" in last_name.get_attribute("class")
    address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "address"))
    )
    assert "alert-success" in address.get_attribute("class")
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "e-mail"))
    )
    assert "alert-success" in email.get_attribute("class")
    phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phone"))
    )
    assert "alert-success" in phone.get_attribute("class")
    city = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "city"))
    )
    assert "alert-success" in city.get_attribute("class")
    country = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    assert "alert-success" in country.get_attribute("class")
    job_position = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "job-position"))
    )
    assert "alert-success" in job_position.get_attribute("class")
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company"))
    )
    assert "alert-success" in company.get_attribute("class")
    driver.quit()
