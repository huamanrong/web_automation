__author__ = '10336'
from PageObjects.BasePage import BasePage
from TestDatas.Common_Data import *
import logging
from Common.dir_config import *
import os
import time
from selenium.webdriver.support import expected_conditions as EC
class PersonalHomePage(BasePage):
    #菜单“个人首页”
    menu_personal_home_page_xpath="//a[text()='个人首页']"
    #菜单“我的视频”
    menu_my_video_xpath="//a[text()='我的视频']"
    #菜单“我的订单”
    menu_my_order_xpath="//a[text()='我的订单']"
    #菜单“我的收藏”
    menu_my_collect_xpath="//a[text()='我的收藏']"
    #菜单“我的关注”
    menu_my_focus_xpath="//a[text()='我的关注']"
    #菜单“我的足迹”
    menu_my_footprint_xpath="//a[text()='我的足迹']"
    #菜单“我的资产”
    menu_my_money_xpath="//a[text()='我的资产']"
    #菜单“地址管理”
    menu_address_manage_xpath="//a[text()='地址管理']"
    #菜单“消息中心”
    menu_message_center_xpath="//a[text()='消息中心']"
    #菜单“原创申请”

    #菜单“发布视频”
    menu_publish_video_xpath="//a[text()='发布视频']"