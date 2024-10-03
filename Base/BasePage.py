from threading import Timer

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver



    def click_on_visibility(self, locator):
        try:
            WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located(locator))
            return WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            print("Timeout")

    def enter_text(self, locator, text):
        try:
            return WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            print("Timeout")

    def return_element_text(self, locator):
        return WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located(locator)).text

    def accept_alert(self):
        return WebDriverWait(self.driver, 40).until(ec.alert_is_present()).accept()

    def dismiss_alert(self):
        return WebDriverWait(self.driver, 40).until(ec.alert_is_present()).dismiss()


    def hover_to_element(self, locator):
        action_chains = ActionChains(self.driver)
        element = WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located(locator))
        action_chains.move_to_element(element)
        return action_chains.perform()

    def press_enter(self,locator):
        return WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located(locator)).send_keys(Keys.ENTER)
