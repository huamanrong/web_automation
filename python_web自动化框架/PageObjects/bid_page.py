#Author: xiaojian
#Time: 2018/7/31 22:14

from PageObjects.BasePage import BasePage
import logging
class BidPage(BasePage):

    # 标详情页面 - 投资金额输入处
    invest_moneyInput_xpath = '//input[@data-url="/Invest/invest"]'
    # 标详情页面 - 投标按钮
    invest_moneySubmit_xpath = "//button[text()='投标']"
    # 投资成功弹出框  查看并激动 - 按钮
    invest_success_activeButton_xpath = '//div[contains(@class,"layui-layer-page")]//button'
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup_xpath = '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]'

    #获取用户余额
    def get_userLeftMoney(self):
       #获取金额输入框的data-amount属性值;
       logging.info("标详情页面：获取用户可用余额。")
       return self.get_element_attribute(self.invest_moneyInput_xpath,"data-amount")

    # 投资行为
    def invest(self, money):
        # 输入金额
        logging.info("标页面：投资操作。")
        self.input_text(self.invest_moneyInput_xpath,money,scroll=True)
        # 提交投资
        self.click(self.invest_moneySubmit_xpath,scroll=True)

    #投资成功的弹出框 - 点击查看并激动 - 进入个人页面
    def click_button_on_investSuccessPopup(self):
        # 点击
        logging.info("标页面：投资成功，点击弹出框中的【查看并激活】按钮。")
        self.click(self.invest_success_activeButton_xpath)




