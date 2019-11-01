#Author: xiaojian
#Time: 2018/7/31 22:23

from PageObjects.BasePage import BasePage
import logging

class UserPage(BasePage):
    # 个人可用余额
    user_leftMoney = '//*[@class="personal_info"]//li[@class="color_sub"]'


    #获取用户余额
    def get_userLeftMoney(self):
        logging.info("用户个人页面：获取用户个人余额。")
        money = self.get_text(self.user_leftMoney,scroll=True)
        # 截取数字部分
        money = money.split("元")
        return money[0]