import os
import time
import logging
from appium import webdriver


# 截图
# img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
# time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# screen_save_path = img_folder + time + '.png'
# driver.get_screenshot_as_file(screen_save_path)


def take_screen_shot(name="takeShot", file_name="photo"):
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '7.1.2',
                    'deviceName': 'KIW-AL10',
                    'noReset': True,
                    'appPackage': 'com.xgimi.instruction30',
                    'appActivity': 'com.xgimi.instruction30.net_instruction.ui.SplashActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True
                    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
    time.sleep(3)  # app启动后等待3秒，方便元素加载完成


    '''
    method explain:获取当前屏幕的截图
    parameter explain：【name】 截图的存放的根目录
    parameter explain：【fileName】 截图的后缀名称
    Usage:
        take_screen_shot(name)   #实际截图保存的结果为：目录名称/2018-01-13_17_10_58_fileName.png
    '''
    day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    fq = "..\\"+name+"\\" + day
    # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
    tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    type = '.png'

    if os.path.exists(fq):
        filename = fq + "\\" + tm + "_" + file_name + type
    else:
        os.makedirs(fq)

        filename = fq + "\\" + tm + "_" + file_name + type
        # logging.INF("路径： "+os)
        # logging.info()
    # c = os.getcwd()
    # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
    driver.get_screenshot_as_file(filename)




# take_screen_shot("photo","应用宝")