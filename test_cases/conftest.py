import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utils import config as con

@pytest.fixture(scope="function")
def test_setup(request):
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver.get(con.url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

