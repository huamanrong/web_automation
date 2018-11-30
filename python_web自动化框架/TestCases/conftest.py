import pytest
from selenium import webdriver
from TestDatas.Common_Data import *
from PageObjects.login_page import LoginPage
import time

@pytest.fixture
def login_web():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 1、访问登陆页面
    driver.get(url)
    #driver.set_page_load_timeout(20)
    LoginPage(driver).login(user,passwd)
    yield driver
    #yield之后的代码，为环境清理工作
    driver.quit()

@pytest.fixture
def init_web():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 1、访问登陆页面
    driver.get(url)
    yield driver
    # yield之后的代码，为环境清理工作
    driver.quit()

#给网页添加cookie，使不用登录就可以在登录状态
@pytest.fixture
def add_cookie_to_be_in_login_state(url,cookie_dict):
    '''
    :param url: 想要在登录状态的网页地址
    :param cookie_dict: 比如{'name' : 'foo', 'value' : 'bar'}，如果cookie有多个，就用元组传入
    :return:
    '''
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    if type(cookie_dict) == tuple:
        for cookie in cookie_dict:
            driver.add_cookie(cookie)
    else:
        driver.add_cookie(cookie_dict)

@pytest.fixture(scope="class")
def test_class():
    print("我是class级别的fixture!!")


@pytest.fixture(scope="session")
def hello():
    print("我是sesison级别的fixture！！！！")


