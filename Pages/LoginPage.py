from selenium.webdriver.common.by import By
from Base.BasePage import BaseDriver

class LoginDriver(BaseDriver):
    user_textbox = (By.CSS_SELECTOR, "#userId")
    continue_btn = (By.CSS_SELECTOR, "#continue")
    pwd_box = (By.CSS_SELECTOR, "#pwd")
    loginHome_btn = (By.CSS_SELECTOR, "#Home")
    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

    def login_to_app(self,user,pass_key):
        self.enter_text(self.user_textbox, user)
        self.press_enter(self.user_textbox)
        self.enter_text(self.pwd_box, pass_key)
        self.click_on_visibility(self.loginHome_btn)

