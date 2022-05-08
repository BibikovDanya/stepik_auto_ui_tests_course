from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time


driver_service = Service(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
url = 'http://suninjuly.github.io/selects1.html'

try:
    # driver = webdriver.Chrome(
    #     executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")

    # Открываем страницу
    driver.get(url)
    # print("get...")

    # Находим числа
    num1 = driver.find_element(By.ID, "num1").text
    num2 = driver.find_element(By.ID, "num2").text


    # Считаем сумму чисел
    def calc():
        sum = str(int(num1) + int(num2))
        return sum


    sum = calc()

    # num1 = int(num1)
    # num2 = int(num2)
    # sum = str(num1 + num2)

    # Указываем список
    select = Select(driver.find_element(By.ID, "dropdown"))
    # driver.find_element(By.ID, "dropdown").click()

    # select.select_by_value("sum")

    # Выбираем необходимый элемент из списка
    driver.find_element(select.select_by_value(sum)).click()

    # Нажимаем на кнопку Submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    # driver.find_element(By.TAG_NAME,".btn").click()


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

if __name__ == '__main__':
    main()

