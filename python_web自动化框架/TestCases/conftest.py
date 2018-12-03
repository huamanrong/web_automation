import pytest
from selenium import webdriver
from TestDatas.Common_Data import *
from PageObjects.login_page import LoginPage
from Common.dir_config import screenshot_dir
import time
import os

driver=None

@pytest.fixture
def login_web():
    global driver
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
    global driver
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
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    if type(cookie_dict) == tuple:
        for cookie in cookie_dict:
            driver.add_cookie(cookie)
    else:
        driver.add_cookie(cookie_dict)
    yield driver
    driver.quit()

#往pytest的测试报告中，当失败的时候 ，添加截图
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            #截屏路径--相对路径
            temp_name = report.nodeid.split("/")[-1]
            file_name = os.path.join(screenshot_dir,temp_name.replace("::", "_")+".png")
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.fixture(scope="class")
def test_class():
    print("我是class级别的fixture!!")


@pytest.fixture(scope="session")
def hello():
    print("我是sesison级别的fixture！！！！")


