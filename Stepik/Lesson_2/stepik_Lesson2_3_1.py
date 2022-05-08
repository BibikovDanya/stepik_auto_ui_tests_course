from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = 'http://suninjuly.github.io/alert_accept.html'

try:
    # открываем страницу
    driver.get(url)
    # нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    # подтверждаем
    driver.switch_to.alert.accept()
    # принимаем x
    x = driver.find_element(By.ID, "input_value").text


    # считаем математическую функцию от x
    def fx():
        fx = str(math.log(abs(12 * math.sin(int(x)))))
        return fx


    fx = fx()
    # находим поле ввода и вводим значение
    driver.find_element(By.ID, "answer").send_keys(fx)

    # нажимаем submit
    driver.find_element(By.CSS_SELECTOR, ".btn")


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
