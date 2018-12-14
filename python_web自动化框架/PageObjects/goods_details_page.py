__author__ = '10336'
from PageObjects.BasePage import BasePage
import logging
class GoodsDetailPage(BasePage):
    #商品规格——一级
    goods_specifications_1_xpath="//li[text()='18岁']"
    #商品规格——二级
    goods_specifications_2_xpath="//li[text()='18岁']"
    #商品数量 + 按钮
    goods_num_add_button_xpath="//span[@class='num-add']"
    #加入购物车按钮
    add_shopping_cart_button_xpath="//a[@class='join-cart login']"
    #立即购买按钮
    buy_now_button_xpath="//a[text()='立即购买']"
    #导航栏的购物车按钮
    head_shopping_cart_button="//li[@class='nav-cart']//a[contains(text(),'购物车')]"


    #选择规格，选择数量为3
    def choose_specifications_and_num(self):
        self.click(self.goods_specifications_1_xpath)
        self.click(self.goods_specifications_2_xpath)
        self.click(self.goods_num_add_button_xpath)
        self.click(self.goods_num_add_button_xpath)

    #点击加入购物车
    def add_shopping_cat(self):
        self.click(self.add_shopping_cart_button_xpath)

    #点击导航栏的购物车按钮
    def click_head_shopping_cart(self):
        self.click(self.head_shopping_cart_button)