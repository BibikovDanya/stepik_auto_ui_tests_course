from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math

a = str(math.ceil(math.pow(math.pi, math.e)*10000))

# url = "http://suninjuly.github.io/simple_form_find_task.html"
link = "http://suninjuly.github.io/find_link_text"
try:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(link)
    # time.sleep(2)
    link = driver.find_element(By.LINK_TEXT,a)
    link.click()
    input1 = driver.find_element(By.NAME,"first_name").send_keys("Ivan")
    # input1 = driver.find_element_by_name("first_name")
    # input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME,"last_name").send_keys("Petrov")
    # input2 = driver.find_element_by_name("last_name")
    # input2.send_keys("Petrov")
    input3 = driver.find_element(By.NAME,"firstname").send_keys("Smolensk")
    # input3 = driver.find_element_by_name("firstname")
    # input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID,"country").send_keys("Russia")
    # input4 = driver.find_element_by_id("country")
    # input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
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


