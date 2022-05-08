from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = 'http://suninjuly.github.io/file_input.html'
try:

    # открываем страницу
    driver.get(url)
    # заполняем обязательные поля
    driver.find_element(By.NAME, "firstname").send_keys("firstname")
    driver.find_element(By.NAME, "lastname").send_keys("lastname")
    driver.find_element(By.NAME, "email").send_keys("test@gmai.com")
    # загружаем файл
    #file_path = os.path.join("C:\\Users\\Алёна\\PycharmProjects\\Selenium\\Stepik\\Lesson_2\\test1.txt", "test1.txt")
    driver.find_element(By.ID,"file").send_keys("C:\\Users\\Алёна\\PycharmProjects\\Selenium\\Stepik\\Lesson_2\\test1.txt")

    # Нажимаем на кнопку Submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


# Выводим ошибки
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # копируем код
    time.sleep(7)
    # закрываем браузер
    driver.close()
    time.sleep(2)
    driver.quit()