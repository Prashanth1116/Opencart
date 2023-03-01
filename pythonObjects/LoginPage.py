from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # FINDING_WEB_OPTIONS

    def get_email(self):
        return self.driver.find_element(By.XPATH, "//input[@id='input-email']")

    def get_password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='input-password']")

    def get_loginOption(self):
        return self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg hidden-xs']")

    def get_warning_message_for_login(self):
        return self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")

    # ACTION_PERFORMANCE_OPTIONS

    def enter_email(self, email_text):
        self.get_email().send_keys(email_text)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def click_on_loginOption(self):
        self.get_loginOption().click()

    def display_warning_message_for_login(self):
        return self.get_warning_message_for_login().text
