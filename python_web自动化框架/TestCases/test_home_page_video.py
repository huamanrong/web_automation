__author__ = '10336'
import pytest
import time
import logging
from PageObjects.home_page import HomePage
from PageObjects.video_details_page import VideoDetailPage

class Test_Home_Page_video:

    #点击首页的原创精选的视频 封面 查看视频(会新增页面)  验证视频时长、视频标题、作者，视频封面是一样的
    @pytest.mark.gg
    @pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
    def test_click_original_selected_picture(self,add_cookie_to_be_in_login_state):
        home=HomePage(add_cookie_to_be_in_login_state)
        dict_home=home.get_original_selected_title_authors_picture_time()
        #点击封面图
        home.click_original_selected_video_picture()
        print('页面跳转成功')
        video_details=VideoDetailPage(add_cookie_to_be_in_login_state)
        print('创建对象成功')
        dict_video=video_details.get_video_title_authors_picture()
        print('获得对象成功')
        # video_time=video_details.click_video_get_video_time()
        assert dict_home['title'] == dict_video['title']
        assert dict_home['authors'] == dict_video['authors']
        # assert dict_home['picture']  in dict_video['picture']
        # assert dict_home['time'] == video_time

    #点击首页的原创精选的视频 标题 查看视频(会新增页面)  验证视频时长、视频标题、作者，视频封面是一样的
    @pytest.mark.gg
    @pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
    def test_click_original_selected_title(self,add_cookie_to_be_in_login_state):
        home=HomePage(add_cookie_to_be_in_login_state)
        dict_home=home.get_original_selected_title_authors_picture_time()
        #点击标题
        home.click_original_selected_video_title()
        video_details=VideoDetailPage(add_cookie_to_be_in_login_state)
        dict_video=video_details.get_video_title_authors_picture()
        # video_time=video_details.click_video_get_video_time()
        assert dict_home['title'] == dict_video['title']
        assert dict_home['authors'] == dict_video['authors']
        # assert dict_home['picture']  == dict_video['picture']

    #点击首页的原创精选两旁的< >切换视频 验证对比视频标题变化
    @pytest.mark.gg
    @pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
    def test_click_original_selected_left_arrow(self,add_cookie_to_be_in_login_state):
        home=HomePage(add_cookie_to_be_in_login_state)
        first_title=home.get_original_selected_ninth_or_fifth_title(1)
        home.click_original_selected_left_arrow()
        time.sleep(2)
        ninth_title=home.get_original_selected_ninth_or_fifth_title(9)
        home.click_original_selected_right_arrow()
        time.sleep(2)
        home.click_original_selected_right_arrow()
        time.sleep(2)
        fifth_title=home.get_original_selected_ninth_or_fifth_title(5)
        assert first_title != ninth_title !=fifth_title

    #3.点击首页的视频分类的音乐分类，点击第一个视频的视频 封面 查看视频(会新增页面)  视频标题、作者是一样的
    def test_(self):
        pass

































