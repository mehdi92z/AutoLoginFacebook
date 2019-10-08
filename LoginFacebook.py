from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class user:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Firefox()
    def login(self):
        driver=self.driver
        driver.get('https://www.facebook.com/')
        time.sleep(2)
        email = driver.find_element_by_id('email')
        email.clear()
        email.send_keys(self.username)
        password = driver.find_element_by_id('pass')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

#program

mehdi = user('username','password')
mehdi.login()
