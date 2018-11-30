#Author: xiaojian
#Time: 2018/7/31 20:59

from PageObjects.BasePage import BasePage
import logging

class HomePage(BasePage):
    #用户昵称
    user_nickname_xpath = '//a[@href="/Member/index.html"]'
    #抢投标按钮
    bid_xpath = '//a[text()="抢投标"]'

    #获取用户昵称
    def get_nickname(self):
        logging.info("首页：获取用户昵称！")
        return self.get_text(self.user_nickname_xpath)

    #点击第一个标的抢投标按钮
    def click_firstBid(self):
        logging.info("首页：点击第一个标的投抢标按钮。")
        self.click(self.bid_xpath,scroll=True)