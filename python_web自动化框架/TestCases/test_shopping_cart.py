__author__ = '10336'
from PageObjects.home_page import HomePage
from PageObjects.mall_page import MallPage
from PageObjects.goods_details_page import GoodsDetailPage
from PageObjects.shopping_cart_page import ShoppingCartPage
import pytest

class Test_Shopping_cart:

    @pytest.mark.gg
    @pytest.mark.usefixtures('login_web')
    def test_shopping_cart(self,login_web):
        home=HomePage(login_web)
        home.click_head_mall_button()
        mall=MallPage(login_web)
        mall.search_goods()
        mall.click_goods_picture()
        details=GoodsDetailPage(login_web)
        details.choose_specifications_and_num()
        details.add_shopping_cat()
        details.click_head_shopping_cart()
        shopping_cart_page=ShoppingCartPage(login_web)
        sku_num=shopping_cart_page.get_goods_sku_num()
        nick_shopping_cart=shopping_cart_page.get_nickname_of_shopping_cart()
        head_nickname=shopping_cart_page.get_head_nickname()
        shopping_cart_page.check_all_choose()
        selected_goods=shopping_cart_page.get_selected_goods_num()
        shopping_cart_beside_num=shopping_cart_page.nick_of_shopping_beside_num()
        assert str(shopping_cart_beside_num) == str(sku_num)
        assert head_nickname in nick_shopping_cart
        assert str(selected_goods) == str(sku_num)



