import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time     

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.chrome.webdriver.WebDriver(executable_path='C:\chromedriver_win32\chromedriver.exe')

    def testLogin(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/login")
        user = driver.find_element(By.NAME,'username')
        user.send_keys("tomsmith")
        time.sleep(3)

        password = driver.find_element(By.NAME,"password")
        password.send_keys("SuperSecretPassword!")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
    def tearDown(self):
        self.driver.close


if __name__ == '__main__':
    unittest.main()



