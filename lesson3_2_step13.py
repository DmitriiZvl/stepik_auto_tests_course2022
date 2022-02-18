import unittest
import time
from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
        input3.send_keys("lol@Slol.com")

        time.sleep(5)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "kakaia to hernia")
        time.sleep(5)
        

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input[contains(@class, 'first') and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[contains(@class, 'second') and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[contains(@class, 'third') and @required]")
        input3.send_keys("lol@Slol.com")

        time.sleep(5)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "kakaia to hernia")
        time.sleep(5)
        
        
if __name__ == "__main__":
    unittest.main()

   # self.assertEqual('что должно быть', 'что есть', 'что произошло');