from selenium import webdriver
import time
import math

a = str(math.ceil(math.pow(math.pi, math.e)*10000))

# url = "http://suninjuly.github.io/simple_form_find_task.html"
link = "http://suninjuly.github.io/find_link_text"
try:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Алёна\\PycharmProjects\\Selenium\\chromedriver\\chromedriver.exe")
    driver.get(link)
    link = driver.find_element_by_link_text(a)
    link.click()
    # input1 = driver.find_element(by=By.NAME, name="first_name")
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    # input2 = driver.find_element(by=By.NAME, name="last_name")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    # input3 = driver.find_element_by(by=By.CLASS_NAME,classname="form-control city")
    input3 = driver.find_element_by_name("firstname")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
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


