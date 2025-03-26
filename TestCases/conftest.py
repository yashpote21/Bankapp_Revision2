import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://apps.credence.in/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



@pytest.fixture(params=[
    ('Admin', 'pass'),
    ('Yashp', 'pass'),
    ('Tushar', 'pass'),
    ('YashPote', 'fail'),
    ('TusharK', 'fail')
])
def Get_DataFor_SearchUser(request):
    return request.param
