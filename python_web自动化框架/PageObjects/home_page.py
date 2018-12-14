__author__ = '10336'
from PageObjects.BasePage import BasePage
from TestDatas.Common_Data import *
import logging
from Common.dir_config import *
import os
import time
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    #导航栏的秀百贝商城
    head_mall_xpath="//li[@class='hot']//a[text()='秀百贝商城']"
    #导航栏的登录按钮
    head_login_xpath="//ul[@class='headNav clearfix']//a[text()='登录']"
    #手机号输入框
    telephone_input_xpath="//input[@class='user mobile']"
    #密码输入框
    pwd_input_xpath="//input[@name='paswrd']"
    #验证码输入框
    verification_code_input_xpath="//input[@id='captchas']"
    #验证码图片
    # verification_code_puiture_xpath="//div[@class='verification']"
    verification_code_puiture_xpath="/html/body/div[4]/div/div/div[2]/div/div[3]/div/div/img"
    #验证码错误提示
    verification_code_wrong="//div[text()='验证码错误']"
    #登录弹窗上面的登录按钮
    window_login_button="//input[@class='btn btn_c']"

    #点击导航栏的登录按钮
    def click_head_login_button(self,use,password):
        self.click(self.head_login_xpath)
        self.input_text(self.telephone_input_xpath,use)
        self.input_text(self.pwd_input_xpath,password)

    #使用导航栏的登录按钮进行登录
    def head_login(self):
        self.find_element(self.verification_code_input_xpath).clear()
        ele_verification_code=self.find_element(self.verification_code_puiture_xpath)
        self.input_text(self.verification_code_input_xpath,self.get_verification_code(ele_verification_code))
        self.click(self.window_login_button)
        time.sleep(1.5)
        if  EC.exists_of_element_located(self.verification_code_wrong).exists(self.driver):
            self.head_login()

    #点击导航栏的“秀百贝商城”
    def click_head_mall_button(self):
        time.sleep(1)
        self.click(self.head_mall_xpath)
















