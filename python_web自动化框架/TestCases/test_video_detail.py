__author__ = '10336'
import pytest
import time
from PageObjects.home_page import HomePage
from PageObjects.video_details_page import VideoDetailPage
from PageObjects.personal_home_page import PersonalHomePage
from PageObjects.personal_center.my_collection_page import MyCollectPage
from PageObjects.head_page import HeadPage
from TestDatas.Common_Data import *


class Test_video_details:
    #验证收藏按钮的状态
    @pytest.mark.gg
    @pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
    def test_collect_button(self,add_cookie_to_be_in_login_state):
        HomePage(add_cookie_to_be_in_login_state).click_original_selected_video_picture()
        video_details=VideoDetailPage(add_cookie_to_be_in_login_state)
        collect_attribute=video_details.get_collect_attribute()
        video_dict=video_details.get_video_title_authors_picture()
        HeadPage(add_cookie_to_be_in_login_state).click_head_nickname()
        PersonalHomePage(add_cookie_to_be_in_login_state).click_menu_my_collect()
        my_collect=MyCollectPage(add_cookie_to_be_in_login_state)
        my_collect.click_menu_video()
        collect_list=my_collect.get_all_video_title()
        if video_dict['title'] in collect_list:
            assert collect_attribute == 'login  act'
        else:
            assert collect_attribute == 'login '

    #进入我的收藏获取标题列表，点击收藏，查看收藏按钮变化,再次进入我的收藏查看变化
    @pytest.mark.gg
    @pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
    def test_click_collect_button(self,add_cookie_to_be_in_login_state):
        HomePage(add_cookie_to_be_in_login_state).click_original_selected_video_picture()
        video_details=VideoDetailPage(add_cookie_to_be_in_login_state)
        collect_attribute_1=video_details.get_collect_attribute()
        head=HeadPage(add_cookie_to_be_in_login_state)
        head.click_head_nickname()
        PersonalHomePage(add_cookie_to_be_in_login_state).click_menu_my_collect()
        my_collect=MyCollectPage(add_cookie_to_be_in_login_state)
        my_collect.click_menu_video()
        collect_list_1=my_collect.get_all_video_title()
        head.click_logo()
        HomePage(add_cookie_to_be_in_login_state).click_original_selected_video_picture()
        video_details.click_collect_button()
        time.sleep(1)
        collect_attribute_2=video_details.get_collect_attribute()
        head.click_head_nickname()
        PersonalHomePage(add_cookie_to_be_in_login_state).click_menu_my_collect()
        my_collect.click_menu_video()
        collect_list_2=my_collect.get_all_video_title()
        assert collect_list_1 != collect_list_2
        assert collect_attribute_1 != collect_attribute_2

    #进行一级评论，带图片
    @pytest.mark.bb
    @pytest.mark.usefixtures('login_web')
    def test_comment_with_picture(self,login_web):
        home=HomePage(login_web)
        home.click_music_classify_left_video_picture()
        video_details=VideoDetailPage(login_web)
        video_details.publish_level_1_comments_with_picture('hahahahah你好',picture_xpath)
        time.sleep(3)
        assert True





