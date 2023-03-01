from selenium.webdriver.common.by import By


class Account:

    def __init__(self, driver):
        self.driver = driver

    # FINDING_WEB_OPTIONS

    def get_account_option(self):
        return self.driver.find_element(By.XPATH, "//h2[normalize-space()='Account']")

    # ACTION_PERFORMANCE_OPTIONS

    def account_text(self):
        return self.get_account_option().text
