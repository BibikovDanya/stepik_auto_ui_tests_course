from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/huge_form.html"
try:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(url)
    elements = driver.find_elements(By.CSS_SELECTOR,"input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.close()
    time.sleep(2)
    driver.quit()


