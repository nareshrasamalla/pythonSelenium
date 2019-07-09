import datetime
import logging
import os

# import pyautogui
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utilities.global_variables import GlobalVariables

logging.basicConfig(level=logging.INFO)


class LoginError(RuntimeError):
    pass


class Login():
    tours_test_url = 'http://newtours.demoaut.com/'


class BaseUI():
    global driver

    def launch_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(
            '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
        driver = webdriver.Chrome(executable_path='D:/NMI_Auto/resources/chromedriver', chrome_options=options)

        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(Login.tours_test_url)
        return driver

    def get_date_time(self):
        """Return date_time"""
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)

    # def take_screenshot(self, screenshot_name):
    #     date_time = self.get_date_time()
    #     if not os.path.exists(GlobalVariables.screenshot_path):
    #         os.makedirs(GlobalVariables.screenshot_path)
    #     pic = pyautogui.screenshot()
    #     pic.save(GlobalVariables.screenshot_path + '\\' + screenshot_name + date_time + '.png')

    def close_browser(self, driver):
        driver.quit()

    def login_application(self, driver, login_type):
        if login_type not in Login.logins_dict.keys():
            logging.info(" Entered In valid login type")
            raise LoginError("account type not in our list")

        username, password = Login.logins_dict[login_type]
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#login").click()
        return
