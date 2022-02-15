from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    
    alert = browser.switch_to.alert
    alert.accept()

    elem = browser.find_element_by_id('input_value').text
    result = str(math.log(abs(12*math.sin(int(elem)))))
    browser.find_element_by_id('answer').send_keys(result)
    
    browser.find_element_by_css_selector("button.btn").click()
    
finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла