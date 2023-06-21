import allure
import pytest

from common.send_appium import SendAppium
# from common.yaml_util import YamlUtil  # yaml数据驱动,缺点:yaml文件会出现重复性代码
from common.parameterize_util import read_testcase  # yaml数据驱动,优点:对yaml文件会出现重复性代码进行优化


@allure.feature("有道云新增模块")
@allure.parent_suite("有道云新增模块")
@allure.suite("有道云新增模块测试用例")
@allure.sub_suite("有道云新增模块测试用例执行情况")
@allure.description('有道云新增模块测试用例 执行人：小明同学')
class TestUI:
    # 这里有个问题就是别的.py文件执行时不会调用,而我们需要的是对所有的测试用例生效,怎么解决? == 调用公共的处理方法执行
    # def setup(self):
    #     table = YamlUtil().read_all_yaml("\\test_case\\Youdao_Cloud\\test_youdao_01.yaml")
    #     self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', table[0]['caps'])
    #     self.driver.implicitly_wait(10)
    #     el = WebDriverWait(self.driver, 3, 1).until(
    #         lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))
    #     if el:
    #         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    # 0.0 打开有道云App并允许读取系统...
    # @pytest.mark.parametrize("onOpen",  YamlUtil().read_all_yaml("test_youdao_01.yaml"))
    # def test_youdao_01(self, onOpen):
    #     # table = YamlUtil().read_all_yaml("test_youdao_01.yaml")
    #     self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', onOpen['caps'])
    #     self.driver.implicitly_wait(10)
    #     el = WebDriverWait(self.driver, 3, 1).until(
    #         lambda x: x.find_element_by_id(onOpen['positioning']))
    #     if el:
    #         self.driver.find_element_by_id(onOpen['positioning']).click()

    # 0.1 打开有道云App并允许读取系统...(优化:yaml文件多余的重复性代码)
    # @pytest.mark.parametrize("onOpen", read_testcase("Youdao_Cloud\\test_youdao_02.yaml"))
    # def test_youdao_01(self, onOpen):
    #     self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', onOpen['data'])
    #     self.driver.implicitly_wait(10)
    #     el = WebDriverWait(self.driver, 3, 1).until(
    #         lambda x: x.find_element_by_id(onOpen['positioning']))
    #     if el:
    #         self.driver.find_element_by_id(onOpen['positioning']).click()


    @pytest.mark.parametrize("AddNotes", read_testcase("Youdao_Cloud\\test_youdao_03.yaml"))
    def test_youdao_01(self, AddNotes):
        SendAppium(AddNotes).standard_yaml()
        # self.driver.find_element_by_id("com.youdao.note:id/add_note").click()  # 点击新增
        # self.driver.find_element_by_id("com.youdao.note:id/add_note_floater_add_note").click()  # 新建笔记
        # if item[0] == "1":
        #     self.driver.find_element_by_id("com.youdao.note:id/btn_cancel").click()
        # self.driver.find_element_by_xpath(
        #     "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys(item[2])
        # self.driver.find_element_by_id("com.youdao.note:id/note_title").send_keys(item[1])  # 标题
        # self.driver.find_element_by_id("com.youdao.note:id/actionbar_complete_text").click()  # 确定
        # title = self.driver.find_element_by_id("com.youdao.note:id/title").text
        # if title == item[1]:
        #     print(f"新增笔记{item[0]}-成功")
        # else:
        #     print(f"新增笔记{item[0]}-失败")
