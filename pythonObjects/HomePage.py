from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_login_option(self):
        return self.driver.find_element(By.XPATH, "//a[@class='btn btn-link navbar-btn']")

    def click_on_login_option(self):
        self.get_login_option().click()
