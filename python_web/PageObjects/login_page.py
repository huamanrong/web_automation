#Author: xiaojian
#Time: 2018/7/31 20:24

from PageObjects.BasePage import BasePage
from Common import logger
import logging

class LoginPage(BasePage):
    # 输入框
    login_user_xpath = '//input[@name="phone"]'
    # 密码输入框
    login_passwd_xpath = '//input[@name="password"]'
    # 按钮
    login_button_xpath = "//button"
    #错误提示框 - 登陆区域
    msg_loginArea_xpath = '//div[@class="form-error-info"]'


    def login(self,username,passwd):
        logging.info("登陆页面：登陆功能。")
        self.input_text(self.login_user_xpath,username)
        self.input_text(self.login_passwd_xpath,passwd)
        self.click(self.login_button_xpath)

    #获取错误提示信息 - 登陆区域的
    def get_errorMsg_fromLoginArea(self):
        logging.info("登陆页面：获取登陆区域弹出的错误提示信息。")
        return self.get_text(self.msg_loginArea_xpath)