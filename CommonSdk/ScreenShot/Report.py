# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 11:26
# @File    : aaa.py
# @Author  : 守望@天空~
"""HTMLTestRunner 截图版示例 appium版"""
import time
from webbrowser import browser

from appium import webdriver
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

from selenium.webdriver.common.keys import Keys


class case_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = 'com.xgimi.instruction30'
        desired_caps['appActivity'] = 'com.xgimi.instruction30.net_instruction.ui.SplashActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """ 手机QQ截图"""
        # self.driver.get
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # browser=self.browser
        # browser.get(self.base_url+'/')
        # u"""百度云登录"""
        browser.find_element_by_name("userName").clear()
        username=browser.find_element_by_name("userName")
        username.send_keys("alu***")
        username.send_keys(Keys.TAB)
        time.sleep(2)
        password=browser.find_element_by_name("password")
        password.send_keys("***")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.close()

    def test_case2(self):
        """ 手机QQ截图"""
        pass
        # self.driver.get
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # browser=self.browser
        # browser.get(self.base_url+'/')
        # u"""百度云登录"""
        # browser.find_element_by_name("userName").clear()
        # username=browser.find_element_by_name("userName")
        # username.send_keys("alu***")
        # username.send_keys(Keys.TAB)
        # time.sleep(2)
        # password=browser.find_element_by_name("password")
        # password.send_keys("***")
        # password.send_keys(Keys.ENTER)
        # time.sleep(3)
        # browser.close()


class case_02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = 'com.xgimi.instruction30'
        desired_caps['appActivity'] = 'com.xgimi.instruction30.net_instruction.ui.SplashActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """ 手机QQ截图"""
        pass
        # self.driver.get
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # browser=self.browser
        # browser.get(self.base_url+'/')
        # u"""百度云登录"""
        # browser.find_element_by_name("userName").clear()
        # username=browser.find_element_by_name("userName")
        # username.send_keys("alu***")
        # username.send_keys(Keys.TAB)
        # time.sleep(2)
        # password=browser.find_element_by_name("password")
        # password.send_keys("***")
        # password.send_keys(Keys.ENTER)
        # time.sleep(3)
        # browser.close()

    def test_case2(self):
        """ 手机QQ截图"""
        pass
        # self.driver.get
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # self.add_img()
        # browser=self.browser
        # browser.get(self.base_url+'/')
        # u"""百度云登录"""
        browser.find_element_by_name("userName").clear()
        username=browser.find_element_by_name("userName")
        username.send_keys("alu***")
        username.send_keys(Keys.TAB)
        time.sleep(2)
        password=browser.find_element_by_name("password")
        password.send_keys("***")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        browser.close()
# 仿佛附近


if __name__ == "__main__":
    suiteAll = unittest.TestSuite()
    test1 = unittest.TestLoader().loadTestsFromTestCase(case_01)
    test2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suiteAll.addTest(test1)
    suiteAll.addTest(test2)
    runer = HTMLTestRunner(title="带截图的测试报告", description="测试描述", stream=open("电子说明书测试报告96.html", "wb"), verbosity=2, retry=1, save_last_try=True)
    runer.run(suiteAll)



"""

这里的verbosity是一个选项,表示测试结果的信息复杂度，有三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
什么都不加就是 verbosity=1


在实例化HTMLTestRunner 对象时追加参数，retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果。

"""