import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    f_name.send_keys('Fggg')
    l_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    l_name.send_keys('Fggg')
    email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    email.send_keys('Fggg@test.ru')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()