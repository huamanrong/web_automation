__author__ = '10336'
from PageObjects.BasePage import BasePage
import logging
class MallPage(BasePage):
    #商品搜索框
    goods_search_box_xpath="//input[@id='search']"
    #搜索按钮
    goods_search_button_xpath="//i[@class='s-icon i-search']"
    #商品图片
    goods_picture_xpath="//div[@class='goods-pic']"

    #搜索商品
    def search_goods(self):
        self.input_text(self.goods_search_box_xpath,'妲己')
        self.click(self.goods_search_button_xpath)

    #点击选择商品的图片,并等待新窗口打开
    def click_goods_picture(self):
        current_handles=self.driver.window_handles
        self.click(self.goods_picture_xpath)
        self.wait_new_window_is_opened(current_handles)
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])