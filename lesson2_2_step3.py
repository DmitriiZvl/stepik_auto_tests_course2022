from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1').text #берем текст из элемента по его айди
    y_element = browser.find_element_by_id('num2').text
    x=int (x_element) #приводим текст в число
    y=int (y_element)
    result =str(x+y) #складываем числа и переводим в текст

    select = Select(browser.find_element_by_tag_name("select"))#выбрать весь селект
    select.select_by_value(result)#найти в селекте вычисленное значение

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    
finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла