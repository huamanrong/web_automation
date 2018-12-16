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
    #原创精选的第一个视频的视频封面
    original_selected_video_picture="//div[@class='tab-cont clearfix']//div[@class='v-img']"
    #原创精选的第一个视频的视频标题
    original_selected_video_title="//div[@class='tab-cont clearfix']//div[@class='v-name']"
    #原创精选两旁的< 箭头
    original_selected_video_left_arrow="//div[@class='v-list headline-b']//li[@class='i-prev ']"
    #原创精选两旁的> 箭头
    original_selected_video_right_arrow="//div[@class='v-list headline-b']//li[@class='i-next ']"
    #原创精选视频的视频时长
    original_selected_video_time="//div[@class='tab-pic']//div[@class='video-bg']/span"
    #原创精选视频的作者
    original_selected_video_author="//div[@class='v-list headline-b']//p"
    #

    #点击导航栏的登录按钮,并输入账号密码
    def click_head_login_button(self,use,password):
        self.click(self.head_login_xpath)
        self.input_text(self.telephone_input_xpath,use)
        self.input_text(self.pwd_input_xpath,password)

    #使用导航栏的登录按钮进行登录，完成自动识别验证码
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

    #点击原创精选视频的封面图
    def click_original_selected_video_picture(self):
        self.click(self.original_selected_video_picture)

    #点击原创精选视频的标题
    def click_original_selected_video_title(self):
        self.click(self.original_selected_video_title)

    #点击原创精选视频的左箭头
    def click_original_selected_left_arrow(self):
        self.click(self.original_selected_video_left_arrow)

    #点击原创精选视频的右箭头
    def click_original_selected_right_arrow(self):
        self.click(self.original_selected_video_right_arrow)

    #获取原创精选的时长
    def get_original_selected_video_time(self):
        self.get_text(self.original_selected_video_time)

    #获取原创精选的标题
    def get_original_selected_title(self):
        self.get_text(self.original_selected_video_title)

    #获取原创精选的作者
    def get_original_selected_authors(self):
        self.get_text(self.original_selected_video_author)

    #获取原创精选的封面图
    def get_original_selected_video_picture(self):
        self.get_element_attribute(self.original_selected_video_picture,'src')
















