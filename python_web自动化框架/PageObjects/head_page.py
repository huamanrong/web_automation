__author__ = '10336'
from PageObjects.BasePage import BasePage

class HeadPage(BasePage):
    #导航栏昵称
    head_nickname_xpath="//li[@class='Unick']/a[@href='/personal-order/home']"
    #导航栏的个人中心
    head_personal_xpath="//ol[@class='nk-cont']//a[@href='/personal-order/home']"
    #导航栏购物车按钮
    head_shopping_cart_xpath="//a[@href='/cart/cart-view' and contains(text(),'购物车')]"
    #导航栏我的订单按钮
    head_my_order_xpath="//a[@href='/personal-order/order-list' and contains(text(),'我的订单')]"
    #导航栏商城按钮
    head_mall_xpath="//a[@href='/mall' and contains(text(),'秀百贝商城')]"
    #logo
    logo_xpath="//img[@src='/image/mall/logo.png']"

    def click_head_nickname(self):
        self.click(self.head_nickname_xpath)

    def click_head_shopping_cart(self):
        self.click(self.head_shopping_cart_xpath)

    def click_head_my_order(self):
        self.click(self.head_my_order_xpath)

    def click_head_mall(self):
        self.click(self.head_mall_xpath)

    def click_logo(self):
        self.click(self.logo_xpath)

