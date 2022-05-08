import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = 'https://SunInJuly.github.io/execute_script.html'

try:
    # открываем страницу
    driver.get(url)

    # считываем значение для переменной x
    x = driver.find_element(By.ID,"input_value").text

    # считаем математическую функцию от x
    def fx():
        fx = str(math.log(abs(12 * math.sin(int(x)))))
        return fx
    fx = fx()

    # прокручиваем страницу
    button = driver.find_element(By.TAG_NAME, "button")
    #driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.execute_script("window.scrollBy(0, 130);")
    # button.click()

    # вводим значение х
    driver.find_element(By.ID, "answer").send_keys(fx)

    # Отмечаем checkbox "I'm the robot"
    driver.find_element(By.ID,"robotCheckbox").click()

    # Выбираем  radiobutton "Robots rule!"
    driver.find_element(By.ID,"robotsRule").click()

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