# coding=UTF-8
'''
Created on 2023.06.19
@author: xM
'''
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from common.yaml_util import YamlUtil


class Singleton(object):
    driver = None
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # super() 是python中调用父类（超类）的一种方法，在子类中可以通过super()方法来调用父类的方法。
            orig = super(Singleton, cls)
            table = YamlUtil().read_all_yaml("\\test_case\\Youdao_Cloud\\test_youdao_01.yaml")
            config = {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'Samsung',
                'newCommandTimeout': 30,
                'automationName': 'UiAutomator2',
                'appPackage': 'com.youdao.note',
                'appActivity': '.activity2.MainActivity'
            # 'autoLaunch':'false'   #appium是否要自动启动或安装APP，默认为ture
            # 'newCommandTimeout':'60'  #设置未接受到新命令的超时时间，默认60s，说明：如果60s内没有接收到新命令，appium会自动断开，如果我需要很长时间做driver之外的操作，可设置延长接收新命令的超时时间
            # 'unicodeKeyboard':True,
            # 'resetKeyboard':True
            # 'noReset':'false'  #在会话前是否重置APP状态，默认是false
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', table[0]['caps'])
            cls._instance.driver.implicitly_wait(10)
            el = WebDriverWait(cls._instance.driver, 3, 1).until(
                lambda x: x.find_element_by_id(table[0]['positioning']))
            if el:
                cls._instance.driver.find_element_by_id(table[0]['positioning']).click()
        return cls._instance


class DriverClient(Singleton):
    def getDriver(self):
        return self.driver