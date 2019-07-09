from selenium.webdriver.common.by import By


class LoginTour:

    def username(self, driver):
        driver.find_element(By.NAME, "userName").send_keys("username")

    def password(self, driver):
        driver.find_element(By.NAME, "password").send_keys("password")

    def submit(self, driver):
        driver.find_element(By.NAME, "login").click()
