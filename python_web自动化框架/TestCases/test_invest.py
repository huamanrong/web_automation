#投资成功用用例
#前置条件 - 已经登陆 - 正确的帐号
#确认当前用户钱够不够？
# --一次性充值很多钱   #接口的方式来执行前置条件
#测试用例 -- 投资50万？？标有没有50万给你投啊。。
#尽量少依赖测试环境 -- 测试环境会变 --
#自动化测试  使用独立的帐号 - 避免其它干扰

#步骤
'''
首页 - 选择第一个标，的抢投标按钮
标页面 - 获取投资前的用户余额 --
标页面 - 输入投资金额，进行投资操作、 投资成功的弹出框
'''
#期望
'''
看个人余额里的钱少了没有  --投资前多少钱 -- 投资后还剩多少钱
投资后 - 个人页面里面的余额
'''
import pytest
from PageObjects.home_page import HomePage
from PageObjects.user_page import UserPage
from PageObjects.bid_page import BidPage
import logging
from TestDatas.invest_data import *

@pytest.mark.usefixtures("login_web")
class Test_Invest:

    @pytest.mark.smoke
    def test_invest_success(self,login_web):
        '''
        首页 - 选择第一个标，的抢投标按钮
        标页面 - 获取投资前的用户余额 --
        标页面 - 输入投资金额，进行投资操作、 投资成功的弹出框
        '''
        HomePage(login_web).click_firstBid()
        bid_p = BidPage(login_web)
        money_beforeInvest = bid_p.get_userLeftMoney()

        bid_p.invest(success_data["invest_money"])
        bid_p.click_button_on_investSuccessPopup()
        #验证
        money_afterInvest = UserPage(login_web).get_userLeftMoney()
        try:
            logging.info("开始比对：比对用户余额是否减少了投资的金额。")
            # assert int(float(money_beforeInvest) - float(money_afterInvest)) == success_data["invest_money"]
            assert False
        except Exception as e:
            logging.exception("比对失败：")
            raise e

