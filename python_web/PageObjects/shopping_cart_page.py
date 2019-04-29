__author__ = '10336'
from PageObjects.BasePage import BasePage
import logging
class ShoppingCartPage(BasePage):
    #商品前面的勾选框
    goods_shoose_box_xpath="//label[@class='goods']"
    #**的购物车旁边的数量
    nickname_of_shopping_beside_num="//h6[@class='cart-tit']//span"
    #**的购物车
    nickname_of_shopping_cart="//h6[@class='cart-tit']"
    #导航栏上的昵称
    head_nickname="//li[@class='Unick']/a"
    #商品数量（计算sku）
    goods_sku_to_get_num="//ul[@class='list-info clearfix']"
    #上面的全选按钮
    above_all_choose="//label[@class='all-che']"
    #下面的全选按钮
    below_all_choose="//label[@class='del-all']"
    #已选商品的数量
    selected_goods_num="//p[text()='已选商品']/span"
    #商品右侧的删除
    goods_right_delete="//span[@class='ic2 delBtn'][1]"
    #底部的删除
    under_delete="//a[@class='delet']"
    #清空失效商品
    empth_unuse_goods="//a[@class='failure']"
    #商品右侧的移入/移除收藏夹
    goods_right_join_collection="//span[@class='ic1 like']"
    #底部的加入收藏夹
    under_collection="//a[@class='favorite']"

    #获取"**的购物车"的文本
    def get_nickname_of_shopping_cart(self):
        return self.get_text(self.nickname_of_shopping_cart)

    #获取导航栏上面的昵称
    def get_head_nickname(self):
        return self.get_text(self.head_nickname)

    #勾选全选按钮，up为上全选，down为下全选
    def check_all_choose(self,up_or_down='up'):
        if up_or_down == 'up':
            self.click(self.above_all_choose)
        else:
            self.click(self.below_all_choose)

    #获得已选商品的数量
    def get_selected_goods_num(self):
        return self.get_text(self.selected_goods_num)

    #获得实际商品sku的数量
    def get_goods_sku_num(self):
        return len(self.driver.find_elements_by_xpath(self.goods_sku_to_get_num))

    #获得**的购物车旁边的数量
    def nick_of_shopping_beside_num(self):
        return self.get_text(self.nickname_of_shopping_beside_num)

