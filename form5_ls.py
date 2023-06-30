from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element(By.ID,"input_value" )
    x = x_element.text
    print (x)
    y = calc(x)
    print (y)

    answer = browser.find_element(By.ID,"answer").send_keys(y)
    
    
    
    c_element = browser.find_element(By.ID,"robotCheckbox" )
    c_element.click()
    
    r_element = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    r_element.click()

    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



