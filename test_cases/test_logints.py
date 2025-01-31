from Pages.LoginPage import LoginDriver
from Utils import config as con,read_excel as exe
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    @pytest.mark.regression
    def test_login_timesheet(self):
        lp = LoginDriver(self.driver)
        lp.login_to_app(con.user, con.pwd)

    @pytest.mark.regression
    @pytest.mark.parametrize("user_name",["Hec\HECIN-EE999","Hec\HECIN-EE9999"])
    def test_login_timesheet_with_different_users(self, user_name):
        lp = LoginDriver(self.driver)
        lp.login_to_app(user_name, con.pwd)

    @pytest.mark.sanity
    @pytest.mark.parametrize("user_name",exe.get_user_data("Data_files/test.xlsx"))
    def test_login_timesheet_with_different_excel_users(self, user_name):
        lp = LoginDriver(self.driver)
        lp.login_to_app(user_name, con.pwd)
