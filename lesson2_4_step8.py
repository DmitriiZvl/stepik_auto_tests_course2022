from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    browser.find_element_by_id('book').click()
    
  

    elem = browser.find_element_by_id('input_value').text
    result = str(math.log(abs(12*math.sin(int(elem)))))
    browser.find_element_by_id('answer').send_keys(result)
    
    browser.find_element_by_id("solve").click()
    
finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла