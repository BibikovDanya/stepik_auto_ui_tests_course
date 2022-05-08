from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(url)

    # Заполняем обязательные поля
    first_name = driver.find_element(By.CSS_SELECTOR,".form-control.first:required",).send_keys("Ivan")

    last_name = driver.find_element(By.CSS_SELECTOR,".form-control.second:required").send_keys("Mikelon")

    email =driver.find_element(By.CSS_SELECTOR,".form-control.third:required").send_keys("Ivanov@gmail.com")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    if  "Congratulations! You have successfully registered!" == welcome_text:
        print("OK")
    else:
        print("WRONG!")

# Выводим ошибки
except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    driver.quit()