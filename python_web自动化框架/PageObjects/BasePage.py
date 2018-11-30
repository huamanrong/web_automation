#Author: xiaojian
#Time: 2018/8/2 21:25
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
from Common.dir_config import *
import logging
import os
import random
from PIL import Image
import pytesseract
from PIL import ImageOps
import win32gui
import win32con
import win32com

class BasePage:

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    #等待元素可见
    def wait_eleVisible(self,locator,by=By.XPATH,wait_times=40):
        if by not in By.__dict__.values():
            logging.error("定位类型[  {0}  ]不在支持类型内。请修改定位类型。".format(by))
            raise InvalidSelectorException
        #开始时间
        t1 = time.time()
        try:
            WebDriverWait(self.driver,wait_times,1).until(EC.visibility_of_element_located((by,locator)))
            t2 = time.time()
            # 结束时间 - 两者之差就是真正的等待时间
            logging.info("等待结束，等待开始时间：{0}，结束等待时间：{1}等待时间长为: {2}".format(t1, t2, t2 - t1))
        except TimeoutException as e:
            logging.exception("等待元素超时.截取当前页面。")
            self.save_screenshot()
            #抛出异常
            raise e
        except InvalidSelectorException as e:
            logging.exception("元素定位表达式：{0}  不正确，请修正".format(locator))

    # 等待元素存在
    def wait_eleExists(self, locator, by=By.XPATH, wait_times=40):
        if by not in By.__dict__.values():
            logging.error("定位类型[  {0}  ]不在支持类型内。请修改定位类型。".format(by))
            raise InvalidSelectorException
        # 开始时间
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times, 1).until(EC.presence_of_element_located((by, locator)))
            t2 = time.time()
            # 结束时间 - 两者之差就是真正的等待时间
            logging.info("等待结束。等待开始时间：{0}，结束等待时间：{1}等待时间长为: {2}".format(t1, t2, t2 - t1))
        except TimeoutException as e:
            logging.exception("等待元素存在超时.截取当前页面。")
            self.save_screenshot()
            # 抛出异常
            raise e
        except InvalidSelectorException as e:
            logging.exception("元素定位表达式：{0}  不正确，请修正".format(locator))


    #查找元素 - 一个元素
    def find_element(self,locator,by=By.XPATH,wait_times=40,type="visible"):
        '''
        :param locator: 元素定位的表达式
        :param by: 元素的定位类型，如id，xpath，name等
        :param wait_times: 等待元素出现或者存在的时长。默认为40s
        :param type: 等待的条件类型。是可见还是元素存在。
                    默认值为visible.目前只考虑可见和存在两种情况 。
        :return: 返回WebElement元素对象。
        '''
        logging.info("当前元素定位类型：{0}，当前查找的元素表达式为：{1}".format(by,locator))
        if type == "visible":
            logging.info("开始等待元素在当前页面可见。")
            self.wait_eleVisible(locator,by,wait_times)
        else:
            logging.info("开始等待元素在当前页面存在。")
            self.wait_eleExists(locator,by,wait_times)
        try:
            ele = self.driver.find_element(by,locator)
            return ele
        except NoSuchElementException as e:
            logging.exception("元素查找失败，找不到该元素。开始截取当前页面图像：")
            self.save_screenshot()
            raise e

    #查找多个元素
    def find_elements(self,locator,by=By.XPATH,wait_times=40,type="visible"):
        logging.info("查找一组元素。元素定位类型：{0}，查找的元素表达式为：{1}".format(by, locator))
        if type == "visible":
            logging.info("开始等待元素在当前页面可见。")
            self.wait_eleVisible(locator,by,wait_times)
        else:
            logging.info("开始等待元素在当前页面存在。")
            self.wait_eleExists(locator,by,wait_times)
        try:
            eles = self.driver.find_elements(by, locator)
            return eles
        except Exception as e:
            logging.exception("元素查找失败。找不到与表达式 {0} 匹配的元素。")
            self.save_screenshot()
            raise e

    # 获取当前页面的url
    def get_url(self):
        return self.driver.current_url

    #滚动到可见区域
    def scroll_intoView(self,ele):
        logging.info("将元素滚动到可见区域。")
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    #元素的点击操作
    def click(self,locator,by=By.XPATH,wait_times=40,type="visible",scroll=False):
        logging.info("=====执行点击事件======")
        ele = self.find_element(locator,by,wait_times,type)
        if scroll is True:
            self.scroll_intoView(ele)
        try:
            ele.click()
        except Exception as e:
            logging.exception("点击操作失败。")
            self.save_screenshot()
            raise e

    def input_text(self,locator,text,by=By.XPATH,wait_times=40,type="visible",scroll=False):
        '''
        :param locator:
        :param text:
        :param by:
        :param wait_times:
        :param type:
        :param scroll:
        :return:
        '''
        logging.info("=====执行输入操作======\n输入的数据为：{0}".format(text))
        ele = self.find_element(locator, by, wait_times, type)
        if scroll is True:
            self.scroll_intoView(ele)
        try:
            ele.send_keys(text)
        except Exception as e:
            logging.exception("输入操作失败。")
            self.save_screenshot()
            raise e

    def get_text(self,locator,by=By.XPATH,wait_times=40,type="visible",scroll=False):
        logging.info("=====获取元素的文本内容======")
        ele = self.find_element(locator,by,wait_times,type)
        if scroll is True:
            self.scroll_intoView(ele)
        try:
            return ele.text
        except Exception as e:
            logging.exception("获取元素的文本内容失败：")
            self.save_screenshot()
            raise e

    #获取元素的属性值
    def get_element_attribute(self,locator,atrribute_name,by=By.XPATH,wait_times=40,type="visible",scroll=False):
        logging.info("=====获取元素的属性值：{0}".format(atrribute_name))
        ele = self.find_element(locator,by,wait_times,type)
        if scroll is True:
            self.scroll_intoView(ele)
        try:
            return ele.get_attribute(atrribute_name)
        except Exception as e:
            logging.exception("获取属性值失败：")
            self.save_screenshot()
            raise e

    #处理alert弹出框
    def alert_handler(self,action="accept"):
        #等待alert出现 #
        WebDriverWait(self.driver,10,1).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        message = alert.text
        if action == "accept":
            alert.accept()
        else:
            alert.dismiss()
        return message

    #截图函数
    def save_screenshot(self):
        r = ""
        for index in range(3):
            r += str(random.randint(1000, 10000))
        #截屏
        file_path = os.path.join(screenshot_dir,"{0}.png".format(time.strftime("%Y%m%d_%H%M%S_{0}".format(r))))
        self.driver.save_screenshot(file_path)
        logging.info("已截取当前页面，文件路径：{0}".format(file_path))

    #返回图形验证码的内容
    def get_screen(self,img_element,web_shot_path,img_shot_path):
        '''
        :param img_element: 验证码的元素对象
        :param web_shot_path: 截取验证码所在网页的截图所存放的路径
        :param img_shot_path: 截取验证码的截图所存放的路径
        :return:返回图形验证码的内容
        '''
        self.driver.save_screenshot(web_shot_path)  #截取当前网页，该网页有我们需要的验证码
        location = img_element.location  #获取验证码x,y轴坐标
        size=img_element.size  #获取验证码的长宽
        coord=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        i=Image.open(web_shot_path) #打开截图
        frame4=i.crop(coord)  #使用Image的crop函数，从截图中再次截取我们需要的区域
        image=frame4.point(lambda x: 0 if x<143 else 255)#处理图片上的每个像素点，使图片上每个点“非黑即白”
        borderImage = ImageOps.expand(image,border=20,fill='white')
        borderImage.save(img_shot_path)
        img = Image.open(img_shot_path)
        aa =  pytesseract.image_to_string(img)
        # if aa == "":               #如果识别为空，则再一次识别
        #     img_element.click()
        #     self.get_screen(self.driver)    #递归，再次调用本函数
        str_1=''
        for item in aa:
            if item.isdigit() or item.isalpha():
                str_1+=item
        logging.info("识别的验证码为：%s"%str_1)
        return str_1

    #判断元素是否存在
    def element_exist(self,locator):
        '''
        :param locator: 元素的定位表达式
        :return:元素存在返回True，元素不存在返回False
        '''
        flag=True
        try:
            self.driver.find_element_by_xpath(locator)
            return flag
        except:
            flag=False
            return flag

    #窗口切换
    def switch_window(self,locator):
        #1.获取当前窗口数量，某个操作导致窗口增加，等待窗口增加之后切换到
        current_handles=self.driver.window_handles   #获取操作之前的窗口数量
        self.driver.find_element_by_xpath(locator).click()  #某个操作来导致窗口数量增加
        #等待新窗口出现，等待方法：比较操作之后的窗口比之前的窗口数量多
        WebDriverWait(self.driver,10,1).until(EC.new_window_is_opened(current_handles))
        handles=self.driver.window_handles   #获取最新的窗口
        self.driver.switch_to.window(handles[-1])    #切换到最后一个窗口也就是最新增加的窗口
        logging.info('窗口已切换')
        # handle=driver.current_window_handle     #返回当前窗口
        # driver.switch_to.window(handle[0])     #返回到之前的窗口

    #iframe切换
    def switch_iframe(self,locator_to_appear_frame,name_iframe):
        #某个操作导致iframe出现，切换到iframe才能操作iframe的元素
        self.driver.find_element_by_xpath(locator_to_appear_frame).click()
        WebDriverWait(self.driver,10,1).until(EC.frame_to_be_available_and_switch_to_it(name_iframe))  #等待iframe出现之后切换到
        logging.info('iframe已切换')
        # self.driver.switch_to.default_content()  #切换到主页面

    #上传文件
    def upload_file(self,file_path):
        #一级窗口
        dialog = win32gui.FindWindow("#32770","打开")
        #二级窗口                            （父节点，0表示从所有子元素找，要找的节点元素，title）
        ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
        #四级窗口 - 文件路径输入框
        edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)
        #二级窗口 - 打开按钮
        button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")
        # #指定要上传的文件路径
        # file_path = r"D:\Backup\桌面\我的\周报\铭勋测试-潘腾虎-工作周报-7月.xlsx"
        #操作 -#发送文件路径
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
        time.sleep(1)
        #点击打开按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    #给网页添加cookie，使不用登录就可以在登录状态
    def add_cookie_to_be_in_login_state(self,url,cookie_dict):
        '''
        :param url: 想要在登录状态的网页地址
        :param cookie_dict: 比如{'name' : 'foo', 'value' : 'bar'}，如果cookie有多个，就用元组传入
        :return:
        '''
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(1)
        if type(cookie_dict) == tuple:
            for cookie in cookie_dict:
                self.driver.add_cookie(cookie)
        else:
            self.driver.add_cookie(cookie_dict)

























