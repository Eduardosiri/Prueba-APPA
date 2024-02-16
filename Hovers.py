import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time     

class hovers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.chrome.webdriver.WebDriver(executable_path='C:\chromedriver_win32\chromedriver.exe')

    def testHovers(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        user = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/img')
        user.click()
        user = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/a')
        user.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close
if __name__ == '__main__':
    unittest.main()