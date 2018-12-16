__author__ = '10336'
from PageObjects.BasePage import BasePage
import time
class VideoDetailPage(BasePage):
    #视频标题
    video_title_xpath="//div[@class='v-tit']/h2"
    #视频封面图
    video_picture_xpath="//div[@class='vjs-poster']"
    #视频时长,播放视频之后才能获取
    video_time_xpath="//span[@class='vjs-remaining-time-display']"
    #收藏按钮
    collect_button_xpath="//div[@class='like fl']//i"
    #视频作者
    video_authors_xpath="//div[@class='store-l fl']//h4"
    #关注按钮
    focus_button_xpath="//div[@class='store-r fr']//a[@href='javascript:;']"
    #进店逛逛
    go_to_personal_page_xpath="//a[text()='进店逛逛>']"
    #评论数
    comments_num_xpath="//div[@class='eva-title']/h2"
    #一级评论输入框
    level_1_comments_input_box_xpath="//textarea[@name='add-textarea']"
    #一级评论添加图片的小图标
    level_1_comments_add_picture_xpath="//input[@name='file']"
    #一级评论添加表情的小图标
    level_1_comments_add_face_xpath="//span[@class='loadexpressionbtn']"
    #评论后面的点赞块
    comments_favour_div_xpath="//div[@class='reply-reply']"
    #评论后面的点赞按钮
    comments_favour_button_xpath="//div[@class='reply-reply']//span[@class='zanbtn']"
    #评论后面的回复按钮
    comments_reply_xpath="//div[@class='reply-reply']//span[@class='replybtn']"
    #一级评论的昵称
    level_1_comments_nickname_xpath="//div[@class='reply-name']"
    #一级评论的时间
    level_1_comments_time_xpath="//span[@class='font-s']"

    #获取视频标题
    def get_video_title(self):
        self.get_text(self.video_title_xpath)

    #获取视频作者
    def get_video_authors(self):
        self.get_text(self.video_authors_xpath)

    #点击收藏按钮,并获取class的属性
    def click_collect_button_get_attribute(self):
        self.click(self.collect_button_xpath)
        return self.get_element_attribute(self.collect_button_xpath,'class')

    #点击关注按钮并获取关注状态
    def click_focus_button_get_attribute(self):
        self.click(self.focus_button_xpath)
        return self.get_text(self.focus_button_xpath)

    #点击进店逛逛，进入个人主页

    #获取评论数

    #发表一级评论

    #获取评论条数

    #发表一级评论带图片

    #发表一级评论带表情

    #获取第一条一级评论的昵称

    #获取第一条评论的时间

    #获取第一条评论的内容

    #对第一条评论进行点赞

    #对第一条评论进行回复

    #





























