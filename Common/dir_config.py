#Author:Xiao Jian

import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]


testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"HtmlTestReport")

logs_dir =  os.path.join(base_dir,"Logs")

config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"ScreenShot")

shot_verification_code_dir=os.path.join(base_dir,"ScreenShot","shot_verification_code")

shot_photo_path=os.path.join(shot_verification_code_dir,'shot.png')
# print(shot_photo_path)

save_photo_path=os.path.join(shot_verification_code_dir,'save.png')