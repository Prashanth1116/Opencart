import time

import pytest
from selenium  import webdriver
from selenium.webdriver.common.by import By

from pythonObjects.Account import Account
from pythonObjects.HomePage import HomePage
from pythonObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class Test_OpenCart:

    def test_TC1(self):  #Login with correct credentials
        home_page = HomePage(self.driver)
        home_page.click_on_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email("18211a1116@bvrit.ac.in")
        login_page.enter_password("Capgemini@933")
        login_page.click_on_loginOption()
        time.sleep(12)
        account_page = Account(self.driver)
        assert account_page.account_text().__eq__("Account")

    def test_TC2(self):  #Login with incorrect mail id
        home_page = HomePage(self.driver)
        home_page.click_on_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email("j.prashanth1116@gmail.com")
        login_page.enter_password("Capgemini@933")
        login_page.click_on_loginOption()
        time.sleep(12)

        assert login_page.display_warning_message_for_login().__contains__("No match for E-Mail and/or Password.")

    def test_TC3(self): #Login with incorrect password
        home_page = HomePage(self.driver)
        home_page.click_on_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email("j.prashanth1116@gmail.com")
        login_page.enter_password("Capgemini@933")
        login_page.click_on_loginOption()
        time.sleep(12)

        assert login_page.display_warning_message_for_login().__contains__("No match for E-Mail and/or Password.")

    def test_TC4(self): #Login without any credentials
        home_page = HomePage(self.driver)
        home_page.click_on_login_option()
        login_page = LoginPage(self.driver)
        login_page.click_on_loginOption()
        time.sleep(12)

        assert login_page.display_warning_message_for_login().__contains__("No match for E-Mail and/or Password.")

    #def test_TC5():
        #home_page = HomePage(self.driver)
        #home_page.click_on_login_option()
        #login_page = LoginPage(self.driver)
        #login_page.click_on_loginOption()

        #driver.find_element(By.XPATH, "//h2[normalize-space()='Request a new password']")


        #e = driver.find_element(By.XPATH, "//h2[normalize-space()='Request a new password']").text.__eq__("Request a new password")
        #if driver.find_element(By.XPATH, "//h2[normalize-space()='Request a new password']").is_displayed():
            #print("True")
        #else:
            #print("False")

