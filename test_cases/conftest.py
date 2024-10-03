import pytest
from selenium import webdriver
from Utils import config as con

@pytest.fixture(scope="function")
def test_setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(con.url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

