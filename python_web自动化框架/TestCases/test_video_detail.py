__author__ = '10336'
import pytest
import time
from PageObjects.home_page import HomePage
from PageObjects.video_details_page import VideoDetailPage

@pytest.mark.gg
@pytest.mark.usefixtures('add_cookie_to_be_in_login_state')
class Test_video_details:
    def test_collect_button(self,add_cookie_to_be_in_login_state):
        video_details=VideoDetailPage(add_cookie_to_be_in_login_state)
