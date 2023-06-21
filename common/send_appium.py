import allure
from selenium.webdriver.support.wait import WebDriverWait

from appium_config import DriverClient
from common.BaseOperate import BaseOperate
from common.logger import GetLogger


class SendAppium:  # 没有参数时可省略()括号
    # 0.初始化
    def __init__(self, data):
        self.driver = DriverClient().getDriver()
        self.test_yaml = data
        self.logger = GetLogger.get_logger()
        self.baseoperate = BaseOperate(self.driver)

    # 1.实现元素定位
    def onLocator(self, loc):  # loc是定位方式和值
        try:
            WebDriverWait(self.driver, 3, 1).until(
                lambda x: x.find_element(*loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    # 2.输入
    def onInput(self, loc, value):
        try:
            self.find_element(*loc).clear()
            self.onLocator(loc).send_keys(value)
        except Exception as e:
            raise e

    # 3.点击
    def onClick(self, loc):
        try:
            self.onLocator(loc).click()
        except Exception as e:
            raise e

    # 4.获取 testcase 的长度,方便后期的遍历
    def caselen(self):
        length = len(self.test_yaml['testcase'])
        return length

    # 5.获取yaml中的定位元素
    def get_elementinfo(self, i):
        return self.test_yaml['testcase'][i]['element_info']

    # 6.获取yaml中定位方式(id,name,xpath,class....)
    def get_findtype(self, i):
        return self.test_yaml['testcase'][i]['find_type']

    # 7.获取yaml中元素触发方式(click\send_keys\text)
    def get_operate_type(self, i):
        return self.test_yaml['testcase'][i]['operate_type']

    # 处理新增逻辑时第二次新增元素变化的处理情况
    def element_index(self, i):
        if self.get_findtype(i) == 'index':
            # print(self.test_yaml['testcase'][i]['element_index'])
            return self.test_yaml['testcase'][i]['element_index']
        else:
            pass

    # 8.获取yaml中元素ids定位方式的 index 值
    def get_index(self, i):
        if self.get_findtype(i) == 'ids':
            return self.test_yaml['testcase'][i]['index']
        else:
            pass

    # 9.获取yaml中元素 send_keys 的输入文本信息
    def get_send_content(self, i):
        if self.get_operate_type(i) == 'send_keys':
            return self.test_yaml['testcase'][i]['send_content']
        else:
            pass

    # 10.获取yaml中元素 的返回或向上滑动的 次数
    def get_backtimes(self, i):
        if self.get_operate_type(i) == 'back' or self.get_operate_type(i) == 'swipe_up':
            return self.test_yaml['testcase'][i]['times']
        else:
            pass

    # 11.获取yaml中测试用例的名称(可用于allure报告的标题...
    def get_title(self):
        return self.test_yaml['testinfo']['Name']

    # 13.规范yaml测试用例
    def standard_yaml(self):
        # print(self.test_yaml)  # {'testinfo': {},'parameterize':{},...}
        caseinfo_keys = self.test_yaml.keys()
        # print(caseinfo_keys)  # dict_keys(['testinfo', 'parameterize', 'testcase', 'validate'])
        # 判断一级关键字是否包含：testinfo(用例描述信息),testcase(元素定位信息),validate(断言信息)
        if "testinfo" in caseinfo_keys and "testcase" in caseinfo_keys and "validate" in caseinfo_keys:
            testName = self.test_yaml['testinfo']['Name']  # 用例名称
            moduleName = self.test_yaml['testinfo']['Module']  # 用例所属模块
            assert_str = self.test_yaml['validate'][0]['contains']  # 用例断言
            data = self.test_yaml['data']  # 用例参数
            # allure用例名称
            allure.dynamic.title(f"{testName}，请求参数:{data}")
            # allure报告用例的描述
            key_list = self.test_yaml['testinfo']['step'].split("/")
            for item in key_list:
                with allure.step(f'{item}'):
                    pass
            print("yaml基本架构规范检查通过")
            self.all_send_appium(testName, moduleName, assert_str, data)
        else:
            print("一级关键字必须包含name,request,validate")

    # 12.统一请求的方法
    def all_send_appium(self, testName, moduleName, assert_str, data=None):
        self.driver.implicitly_wait(10)
        # 将接口发起前的信息记录到日志中
        self.logger.info('----------------appium UI自动化测试开始----------------')
        self.logger.info(f"用例的名称是：{testName}")
        self.logger.info(f"用例的所属模块是：{moduleName}")
        self.logger.info(f'用例的Data是：{data}')

        try:
            for i in range(self.caselen()):
                # 1.处理点击
                if self.get_operate_type(i) == 'click':
                    if self.get_findtype(i) == 'text':
                        self.baseoperate.get_name(self.get_elementinfo(i)).click()
                    elif self.get_findtype(i) == 'id':
                        self.baseoperate.get_id(self.get_elementinfo(i)).click()
                    elif self.get_findtype(i) == 'index':
                        # 处理第二次新增有道云笔记的无法获取元素的情况
                        if self.element_index(i) != '1' and self.get_elementinfo(i) == 'com.youdao.note:id/btn_cancel':
                            pass
                        else:
                            self.baseoperate.get_id(self.get_elementinfo(i)).click()
                    elif self.get_findtype(i) == 'xpath':
                        self.baseoperate.get_xpath(self.get_elementinfo(i)).click()
                    elif self.get_findtype(i) == 'ids':
                        self.baseoperate.get_ids(self.get_elementinfo(i))[self.get_index(i)].click()

                # 2.处理键盘输入
                elif self.get_operate_type(i) == 'send_keys':
                    if self.get_findtype(i) == 'text':
                        self.baseoperate.get_name(self.get_elementinfo(i)).send_keys(self.get_send_content(i))
                    elif self.get_findtype(i) == 'id':
                        self.baseoperate.get_id(self.get_elementinfo(i)).send_keys(self.get_send_content(i))
                    elif self.get_findtype(i) == 'xpath':
                        self.baseoperate.get_xpath(self.get_elementinfo(i)).send_keys(self.get_send_content(i))
                    elif self.get_findtype(i) == 'ids':
                        self.baseoperate.get_ids(self.get_elementinfo(i))[self.get_index(i)].send_keys(
                            self.get_send_content(i))

                # 3.处理手机的返回按键
                elif self.get_operate_type(i) == 'back':
                    for n in range(self.get_backtimes(i)):
                        self.baseoperate.back()

                # 4.处理手机的向上滑动
                elif self.get_operate_type(i) == 'swipe_up':
                    for n in range(self.get_backtimes(i)):
                        self.baseoperate.swipe_up()

                # 5.处理用例完成后的响应信息
                elif self.get_operate_type(i) == 'text':
                    if self.get_findtype(i) == 'text':
                        Response_Text = self.baseoperate.get_name(self.get_elementinfo(i)).text
                    elif self.get_findtype(i) == 'id':
                        Response_Text = self.baseoperate.get_id(self.get_elementinfo(i)).text
                    elif self.get_findtype(i) == 'xpath':
                        Response_Text = self.baseoperate.get_xpath(self.get_elementinfo(i)).text
                    elif self.get_findtype(i) == 'ids':
                        Response_Text = self.baseoperate.get_ids(self.get_elementinfo(i))[self.get_index(i)].text

            self.logger.info(f"用例的响应信息是：{Response_Text}")
            self.logger.info(f"用例的断言信息是：{assert_str}")
            # 断言:
            self.assert_result(self.test_yaml['validate'], Response_Text)  # 调用下面的方法处理
            self.logger.info('----------------appium UI自动化测试结束----------------' + "\n")
        except BaseException as e:
            self.logger.exception('appium 自动化测试报错！')
            raise BaseException(f'报错信息：{e}')

    # 断言
    def assert_result(self, dy_result, return_json):
        # print(f"dy_result:{dy_result}")  # [{'contains': 'xxx'}]
        # print(f"return_json:{return_json}")
        # print(type(return_code))  # int 整型
        all_flag = 0
        for dy in dy_result:
            for key, value in dy.items():
                if key == 'contains':
                    flag = self.contains_assert(value, return_json)  # 调用包含断言
                    all_flag = all_flag + flag
                else:
                    print("框架暂不支持此段断言方式")
        assert all_flag == 0  # True表示断言通过

    # 包含断言
    def contains_assert(self, value, return_json):
        flag = 0
        if value not in str(return_json):  # {'msg': '用户名错误', 'errorCode': 20000}
            flag = flag + 1
            self.logger.info(f"断言失败：返回的结果 {return_json} 中不包含：{value}")
            print("断言失败：返回的结果中不包含：" + value)
        return flag

