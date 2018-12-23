__author__ = '10336'
from PageObjects.BasePage import BasePage
import time

class MyCollectPage(BasePage):
    #商品的菜单
    menu_goods_xpath="//a[text()='商品']"
    #视频的菜单
    menu_video_xpath="//a[text()='视频']"
    #第一个商品的标题
    first_goods_title_xpath="//ul[@class='hotGoods clearfix']/li[1]//div[@class='info-box']//p"
    #第一个商品的图片
    first_goods_picture_xpath="//ul[@class='hotGoods clearfix']/li[1]//div[@class='goods-pic']"
    #第一个商品的块（用来算商品数量的）
    first_goods_div_xpath="//ul[@class='hotGoods clearfix']/li"
    #第一个商品的金额
    first_goods_amount_xpath="//ul[@class='hotGoods clearfix']/li[1]//span"
    #第一个商品的删除按钮
    first_goods_delete_button_xpath="//ul[@class='hotGoods clearfix']/li[1]//i[@class='del']"
    #第一个视频的块（用来算视频数量的）
    first_video_div_xpath="//div[@class='v-list wrap']/ul[@class='clearfix']/li"
    #第一个视频的图片
    first_video_picture_xpath="//div[@class='v-list wrap']/ul[@class='clearfix']/li[1]//div[@class='v-img']"
    #第一个视频的标题
    first_video_title_xpath="//div[@class='v-list wrap']/ul[@class='clearfix']/li[1]//div[@class='v-name']//p"
    #第一个视频的删除按钮
    first_video_delete_button_xpath="//div[@class='v-list wrap']/ul[@class='clearfix']/li[1]//i[@class='det']"
    #第一个视频的作者
    first_video_authors="//div[@class='v-list wrap']/ul[@class='clearfix']/li[1]//p[@class='sp-name']"
    #删除商品/视频之后的确定按钮
    delete_sure_button="//div[@class='popUp-btn']"

    #计算有多少个商品
    def count_goods_num(self):
        return len(self.driver.find_elements_by_xpath(self.first_goods_div_xpath))

    #返回所有商品的标题
    def get_all_goods_title(self):
        num=self.count_goods_num()
        list_1=[]
        for item in range(num):
            locator=self.first_goods_title_xpath.replace('1',str(item+1))
            title=self.get_text(locator)
            list_1.append(title)
        return list_1

    #获取第一个商品的标题和价格
    def get_first_goods_title_amount(self):
        dict_1={}
        dict_1['title']=self.get_text(self.first_goods_title_xpath)
        dict_1['tamount']=self.get_text(self.first_goods_amount_xpath)
        return dict_1

    #点击删除商品按钮，及点击确定
    def delete_goods(self):
        self.click(self.first_goods_delete_button_xpath)
        self.click(self.delete_sure_button)

    #点击视频菜单
    def click_menu_video(self):
        self.click(self.menu_video_xpath)

    #计算有多少个视频
    def count_video_num(self):
        return len(self.driver.find_elements_by_xpath(self.first_video_div_xpath))

    #返回所有视频的标题
    def get_all_video_title(self):
        num=self.count_video_num()
        list_1=[]
        for item in range(num):
            locator=self.first_video_div_xpath.replace('1',str(item+1))
            title=self.get_text(locator)
            list_1.append(title)
        return list_1

    #获取第一个视频的标题和作者
    def get_first_video_title_authors(self):
        dict_1={}
        dict_1['title']=self.get_text(self.first_video_title_xpath)
        dict_1['authors']=self.get_text(self.first_video_authors)