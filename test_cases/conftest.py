import pytest
from selenium import webdriver
from Utils import config as con

@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver.get(con.url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

