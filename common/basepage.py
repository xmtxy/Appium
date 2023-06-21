# ÿ��ҳ����ͬ�����Լ���Ϊ
# from appium.webdriver.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 0.��ʼ��
    def __init__(self, driver):
        self.driver = driver
        # self.caps = {}
        # self.caps['automationName'] = "UiAutomator2"
        # self.caps['platformName'] = "Android"  # ���������ֻ�ϵͳ��ios����Android
        # self.caps['platformVersion'] = '6.0'  # �����ֻ���Android�汾��
        # self.caps['deviceName'] = "Samsung"  # �����ֻ�������
        # self.caps['appPackage'] = "com.youdao.note"
        # self.caps['appActivity'] = '.activity2.MainActivity'
        # self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        # self.driver.implicitly_wait(10)  # ��ʽ�ȴ�
        # el = WebDriverWait(self.driver, 3, 1).until(
        #     lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))  # Ԫ�ش��ڷ���True
        # if el:
        #     self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()  # �������

    # 1.ʵ��Ԫ�ض�λ
    def onLocator(self, loc):  # loc�Ƕ�λ��ʽ��ֵ
        return self.driver.find_element(*loc)

    # 2.����
    def onInput(self, loc, value):
        self.onLocator(loc).send_keys(value)

    # 3.���
    def onClick(self, loc):
        self.onLocator(loc).click()

    # 4.����(�������һ���)
    def onSwipe(self, start_x, start_y, end_x, end_y, duration=0):
        # ��ȡ��Ļ�ĳߴ�
        window_size = self.driver.get_window_size()
        # print(f"�ֻ�����Ļ�ߴ�Ϊ:{window_size}")
        x = window_size['width']
        y = window_size['height']
        self.driver.swipe(start_x=x * start_x, start_y=y * start_y, end_x=x * end_x, end_y=y * end_y, duration=duration)
