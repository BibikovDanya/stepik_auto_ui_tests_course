from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math


driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
url = 'http://suninjuly.github.io/get_attribute.html'

try:
    #driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(url)

    # ищем сундук
    box = driver.find_element(By.ID,"treasure")

    # берем значение атрибута valuex
    vaariable_x = box.get_attribute("valuex")

    # функция подсчета х
    def calc(vaariable_x):
        return str(math.log(abs(12 * math.sin(int(vaariable_x)))))
    # считаем х
    x = calc(vaariable_x)

    # вводим значение х в поле input
    input_x = driver.find_element(By.ID, "answer").send_keys(x)

    # Отмечаем checkbox "I'm the robot"
    driver.find_element(By.ID, "robotCheckbox").click()

    # Выбираем  radiobutton "Robots rule!"
    driver.find_element(By.ID, "robotsRule").click()

    # Нажимаем на кнопку Submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

# Выводим ошибки
except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    # копируем код
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.close()
    time.sleep(2)
    driver.quit()