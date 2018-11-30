from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas.login_testdata import *
import pytest
from Common import logger
import logging
@pytest.mark.login
@pytest.mark.usefixtures("init_web")
class Test_Login:

    @pytest.mark.smoke
    def test_login_success(self,init_web):
        #步骤 # 2、输入用户名、密码、点击登陆
        LoginPage(init_web).login(success_data["username"],success_data["passwd"])
        #结果比对 #3、首页当中的，用户昵称
        try:
            logging.info("断言：比对用户昵称是否相等。")
            assert HomePage(init_web).get_nickname() == success_data["check"]
        except:
            logging.exception("比对失败：")
            raise

    #参数化：无用户名或者无密码.
    # @pytest.mark.parametrize()#方式进行参数化
    #采用标记函数参数化，传入单个参数，pytest.mark.parametrize("参数名"，lists）
    @pytest.mark.parametrize("testDatas",no_data)
    def test_login_noData(self,init_web,testDatas):
        # 步骤 # 2、输入用户名、密码、点击登陆
        lp = LoginPage(init_web)
        lp.login(testDatas["username"], testDatas["passwd"])
        #比对  - 错误提示：请输入密码
        try:
            logging.info("当用户名/密码不正确时，比对提示信息是否正确。")
            assert lp.get_errorMsg_fromLoginArea() == testDatas["check"]
        except:
            logging.exception("比对失败：")
            raise

    # def test_login_wrongPasswd(self):
    #     pass

