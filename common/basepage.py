# 每个页面相同的属性及行为
# from appium.webdriver.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 0.初始化
    def __init__(self, driver):
        self.driver = driver
        # self.caps = {}
        # self.caps['automationName'] = "UiAutomator2"
        # self.caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
        # self.caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
        # self.caps['deviceName'] = "Samsung"  # 测试手机的名称
        # self.caps['appPackage'] = "com.youdao.note"
        # self.caps['appActivity'] = '.activity2.MainActivity'
        # self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        # self.driver.implicitly_wait(10)  # 隐式等待
        # el = WebDriverWait(self.driver, 3, 1).until(
        #     lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))  # 元素存在返回True
        # if el:
        #     self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()  # 点击允许

    # 1.实现元素定位
    def onLocator(self, loc):  # loc是定位方式和值
        return self.driver.find_element(*loc)

    # 2.输入
    def onInput(self, loc, value):
        self.onLocator(loc).send_keys(value)

    # 3.点击
    def onClick(self, loc):
        self.onLocator(loc).click()

    # 4.滑动(上下左右滑动)
    def onSwipe(self, start_x, start_y, end_x, end_y, duration=0):
        # 获取屏幕的尺寸
        window_size = self.driver.get_window_size()
        # print(f"手机的屏幕尺寸为:{window_size}")
        x = window_size['width']
        y = window_size['height']
        self.driver.swipe(start_x=x * start_x, start_y=y * start_y, end_x=x * end_x, end_y=y * end_y, duration=duration)
