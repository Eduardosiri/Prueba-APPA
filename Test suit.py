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

    def testimput(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/inputs")
        user = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/input')
        user.send_keys("4")
        time.sleep(3)

    def tearDown(self):
        self.driver.close

    def testhovers(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/hovers")
        user = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/img')
        user.click()
        user = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/a')
        user.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close

    def testDropdown(self):
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(5)
        user = driver.find_element(By.XPATH,'//*[@id="dropdown"]')
        user.click()
        user= driver.find_element(By.XPATH,'//*[@id="dropdown"]/option[2]')
        user.click()
        time.sleep(5)
        user = driver.find_element(By.XPATH,'//*[@id="dropdown"]')
        user.click()
        user = driver.find_element(By.XPATH,'//*[@id="dropdown"]/option[3]')
        user.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close
if __name__ == '__main__':
    unittest.main()



