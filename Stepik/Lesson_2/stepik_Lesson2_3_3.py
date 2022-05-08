from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

url = 'http://suninjuly.github.io/explicit_wait2.html'

try:

    # открываем страницу
    driver.get(url)

    # говорим WebDriver искать каждый элемент в течение
    driver.implicitly_wait(1)

    # указываем ожидание определенной цены
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))


    # находим и кликаем кнопку

    driver.find_element(By.ID, "book").click()

    # скролим страницу
    # button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("window.scrollBy(0, 460);")

    # принимаем x
    x = driver.find_element(By.ID, "input_value").text


    # считаем математическую функцию от x
    def fx():
        fx = str(math.log(abs(12 * math.sin(int(x)))))
        return fx


    fx = fx()
    # находим поле ввода и вводим значение
    driver.find_element(By.ID, "answer").send_keys(fx)
    time.sleep(1)
    driver.find_element(By.ID,"solve").click()



# Выводим ошибки
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(5)
    # закрываем браузер
    driver.close()
    time.sleep(2)
    driver.quit()
