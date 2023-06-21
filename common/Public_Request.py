from appium.webdriver.webdriver import WebDriver
from time import sleep

# V1.使用脚本在一个模拟器上进行项目的安装
"""
class SendRequest:  # 存储着属性和方法
    def __init__(self):
        self.caps = {}
        self.caps['automationName'] = "UiAutomator2"
        self.caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
        self.caps['platformVersion'] = '7.1.2'  # 测试手机的Android版本号
        self.caps['deviceName'] = "M2007J22C"  # 测试手机的名称
        # self.caps['appPackage'] = "com.android.launcher3"
        # self.caps['appActivity'] = '.launcher3.Launcher'
        self.caps['appPackage'] = "com.youdao.note"  # 被测有道云app的包名
        self.caps['appActivity'] = '.activity2.MainActivity'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    def all_send_request(self):
        el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").is_enabled()
        if el:
            print("安装有道云成功")
        else:
            print("安装有道云失败")
if __name__ == '__main__':  # main是入口函数
    yd = SendRequest()
    yd.all_send_request()
"""
