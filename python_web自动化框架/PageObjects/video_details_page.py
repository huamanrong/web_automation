__author__ = '10336'
from PageObjects.BasePage import BasePage
import time
class VideoDetailPage(BasePage):
    #导航栏昵称
    head_nickname_xpath="//li[@class='Unick']/a[@href='/personal-order/home']"
    #导航栏的个人中心
    head_personal_xpath="//ol[@class='nk-cont']//a[@href='/personal-order/home']"
    #视频标题
    video_title_xpath="//div[@class='v-tit']/h2"
    #视频封面图
    video_picture_xpath="//div[@class='vjs-poster']"
    #视频的播放按钮
    play_video_button_xpath="//button[@class='vjs-big-play-button']"
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
    #一级评论的发表评论按钮
    level_1_publish_comments_button="//div[@class='publishbtn login']"
    #一级评论的字数统计
    level_1_word_num="//div[@class='add-comment clearfix']//span[@class='fontnum']"
    #一级评论添加图片的小图标
    level_1_comments_add_picture_xpath="//input[@name='file']"
    #一级评论添加表情的小图标
    level_1_comments_add_face_xpath="//span[@class='loadexpressionbtn']"
    #第三个表情（笑哭）
    face_xpath="//div[@class='face face_1 icon_3']"
    #评论后面的点赞块
    comments_favour_div_xpath="//div[@class='reply-reply']"
    #评论后面的点赞按钮
    comments_favour_button_xpath="//ul[@class='hot-comments']/li[1]//div[@class='reply-reply']//span[@class='zanbtn']"
    #评论后面的回复按钮
    comments_reply_xpath="//ul[@class='hot-comments']/li[1]//div[@class='reply-reply']//span[@class='replybtn']"
    #一级评论的昵称
    level_1_comments_nickname_xpath="//div[@class='reply-name']"
    #一级评论的时间
    level_1_comments_time_xpath="//span[@class='font-s']"
    #一级评论的文本    获取text
    level_1_comments_content_text_xpath="//ul[@class='hot-comments']/li[1]//div[@class='reply-content']"
    #一级评论的表情    获取text，表情名
    level_1_comments_content_face_xpath="//ul[@class='hot-comments']/li[1]//div[@class='reply-content']/i"
    #一级评论的图片 获取class的属性就行
    level_1_comments_content_picture_xpath="//ul[@class='hot-comments']/li[1]//div[@class='limitimgbox']/img"

    #获取视频标题，作者，图片
    def get_video_title_authors_picture(self):
        dict_1={}
        dict_1['title']=self.get_text(self.video_title_xpath)
        dict_1['authors']=self.get_text(self.video_authors_xpath)
        # dict_1['picture']=self.get_element_attribute(self.video_picture_xpath,'style')
        return dict_1

    #获取视频时长（点击播放时获取）
    def click_video_get_video_time(self):
        self.click(self.play_video_button_xpath)
        return self.get_text(self.video_time_xpath)

    #点击收藏按钮
    def click_collect_button(self):
        self.click(self.collect_button_xpath)

    #获取收藏class的属性
    def get_collect_attribute(self):
        return self.get_element_attribute(self.collect_button_xpath,'class')

    #点击关注按钮并获取关注状态
    def click_focus_button_get_attribute(self):
        self.click(self.focus_button_xpath)
        return self.get_text(self.focus_button_xpath,scroll=True)

    #点击进店逛逛，进入个人主页
    def click_go_to_personal_page(self):
        self.click(self.go_to_personal_page_xpath,scroll=True)

    #获取评论数
    def get_comments_num(self):
        comments=self.get_text(self.comments_num_xpath,scroll=True)
        return comments.replace('评论(','').replace(')','')

    #发表一级评论
    def publish_level_1_comments(self,word):
        self.input_text(self.level_1_comments_input_box_xpath,word,scroll=True)
        self.click(self.level_1_publish_comments_button)

    #获取实际评论条数
    def get_actual_comments_num(self):
        ele=self.find_element(self.comments_favour_div_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        return len(self.driver.find_elements_by_xpath(self.comments_favour_div_xpath))

    #发表一级评论带图片
    def publish_level_1_comments_with_picture(self,word,picture_path):
        self.click(self.level_1_comments_add_picture_xpath,scroll=True)
        self.input_text(self.level_1_comments_input_box_xpath,word,scroll=True)
        time.sleep(2)
        # self.upload_file(picture_path)
        # self.click(self.level_1_publish_comments_button)

    #发表一级评论带表情
    def publish_level_1_comments_with_face(self,word):
        self.input_text(self.level_1_comments_input_box_xpath,word,scroll=True)
        self.click(self.level_1_comments_add_face_xpath)
        self.click(self.face_xpath)
        self.click(self.level_1_publish_comments_button)

    #获取第一条一级评论的昵称、时间
    def get_level_1_comments_nickname_time(self):
        dict_1={}
        dict_1['nickname']=self.get_text(self.level_1_comments_nickname_xpath,scroll=True)
        dict_1['time']=self.get_text(self.level_1_comments_time_xpath)
        return dict_1

    #获取第一条评论的内容
    def get_level_1_comments_content(self):
        dict_1={}
        ele=self.find_element(self.level_1_comments_nickname_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        if self.element_exist(self.level_1_comments_content_text_xpath):
            dict_1['text']=self.get_text(self.level_1_comments_content_text_xpath)
        if self.element_exist(self.level_1_comments_content_face_xpath):
            dict_1['face']=self.get_text(self.level_1_comments_content_face_xpath)
        if self.element_exist(self.level_1_comments_content_picture_xpath):
            dict_1['picture']=self.get_element_attribute(self.level_1_comments_content_picture_xpath,'class')
        return dict_1

    #对第一条评论进行点赞,并返回点赞之前的点赞数
    def give_favour_for_level_1_comments(self):
        num=self.get_text(self.comments_favour_button_xpath,scroll=True)
        if self.find_element(self.comments_favour_button_xpath).is_enabled():
            self.click(self.comments_favour_button_xpath)
        return num

    #对第一条评论进行回复

    #





























