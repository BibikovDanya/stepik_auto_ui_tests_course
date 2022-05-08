from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


url = "http://suninjuly.github.io/find_xpath_form"

try:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(url)
    # time.sleep(2)

    input1 = driver.find_element(By.NAME,"first_name").send_keys("Ivan")

    input2 = driver.find_element(By.NAME,"last_name").send_keys("Petrov")

    input3 = driver.find_element(By.NAME,"firstname").send_keys("Smolensk")

    input4 = driver.find_element(By.ID,"country").send_keys("Russia")

    button = driver.find_element(By.XPATH,"/html/body/div/form/div[6]/button[3]")

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


