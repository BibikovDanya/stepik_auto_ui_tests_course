from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/math.html'

try:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(url)
    # считываем значение х
    vaariable_x = driver.find_element(By.ID,"input_value").text

    # функция подсчета х
    def calc(vaariable_x):
        return str(math.log(abs(12 * math.sin(int(vaariable_x)))))
    # считаем х
    x = calc(vaariable_x)

    # вводим значение х в поле input
    input_x = driver.find_element(By.ID, "answer").send_keys(x)

    # Отмечаем checkbox "I'm the robot"
    checkbox = driver.find_element(By.ID,"robotCheckbox").click()

    # Выбираем  radiobutton "Robots rule!"
    robotsRule = driver.find_element(By.ID, "robotsRule").click()

    # Нажимаем на кнопку Submit
    submit = driver.find_element(By.CSS_SELECTOR,".btn.btn-default").click()



# Выводим ошибки
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    #копируем код
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.close()
    time.sleep(2)
    driver.quit()