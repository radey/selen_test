import unittest
import time
from selenium import webdriver
import random


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://dev.devse.xyz/register")
        #проверяем что перешли на нужную страницу
        self.assertIn("DEMO", driver.title)
        elem1 = driver.find_element_by_xpath(".//img[@alt='DEMO']")
        self.assertEqual(elem1.tag_name, "img")
        #находим элементы страницы регистрации
        elem2 = driver.find_element_by_xpath(".//input[@name='first_name']")
        elem3 = driver.find_element_by_xpath(".//input[@name='last_name']")
        elem4 = driver.find_element_by_xpath(".//input[@name='email']")
        elem5 = driver.find_element_by_xpath(".//input[@name='phone']")
        elem6 = driver.find_element_by_xpath(".//input[@name='password']")
        elem9 = driver.find_element_by_xpath(".//input[@name='password_confirmation']")
        elem7 = driver.find_element_by_xpath('.//div[@class="block mt-4"]//input[@type="checkbox"]')
        elem8 = driver.find_element_by_xpath(".//button[contains(text(),'Регистрация')]")
        if elem1 and elem2 and elem3 and elem4 and elem5 and elem6 and elem7:
            #проверяем что элементы нашлись
            print("all elements found")
        # добавляем в поля регистрационные данные
        elem2.send_keys("picon")
        elem3.send_keys("lkjl")
        mail_string = str(random.randint(0,1000)) #генерим уникальный номер почты
        elem4.send_keys("test"+mail_string+"@test.ru")
        elem5.send_keys("789456123321")
        elem6.send_keys("CDE34rfv")
        elem9.send_keys("CDE34rfv")
        elem7.click() #прожимаем чекбокс
        time.sleep(3)
        elem8.click() #нажимаем кнопку зарегистрироваться
        time.sleep(3)
        test_of_success = driver.find_element_by_xpath(".//button/img[@alt='picon lkjl']")
        self.assertTrue(test_of_success)
        """проверяем что регистрация прошла успешно найдя элемент с именем и фамилией"""
        print("whats all!!")
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()