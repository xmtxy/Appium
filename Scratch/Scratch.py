import csv

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver

from time import sleep
import random  # 导入随机数的包

from common.csv_util import CsvUtil
from common.yaml_util import YamlUtil

"""
# 1.模拟器执行的程序:（常量的传入）
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
caps['deviceName'] = "192.168.110.101:5555"  # 测试手机的名称
caps['appPackage'] = "com.android.calculator2"  # 被测app的包名
caps['appActivity'] = '.Calculator'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()
# 获取实际结果 com.android.calculator2:id/formula
result = driver.find_element_by_id('com.android.calculator2:id/formula').text
if int(result) == 10:
    print("测试通过")
else:
    print("测试失败")
sleep(3)
driver.quit()
"""

"""
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '11'  # 测试手机的Android版本号
caps['deviceName'] = "1da73b4c"  # 测试手机的名称
caps['appPackage'] = "com.miui.calculator"  # 被测app的包名
caps['appActivity'] = '.cal.CalculatorActivity'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
sleep(3)
# com.miui.calculator:id/digit_3
driver.find_element_by_id("com.miui.calculator:id/digit_3").click()
# driver.find_element_by_id('com.youdao.calculator:id/ap_add').click()
# driver.find_element_by_id('com.youdao.calculator:id/digit_7').click()
# driver.find_element_by_id('com.youdao.calculator:id/eq').click()
sleep(3)
driver.quit()

"""


"""
# 2.模拟器执行的程序:（变量的传入->for循环遍历执行）
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
caps['deviceName'] = "192.168.110.101:5555"  # 测试手机的名称
caps['appPackage'] = "com.android.calculator2"  # 被测app的包名
caps['appActivity'] = '.Calculator'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
# 1、变量的显示
# x = int(input("输入第一个数:"))
# y = int(input("输入第二个数:"))
# 2、for循环的方式
for item in range(0, 3):
    # 3、随机数的方式
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    # s = int(item) + int(item)
    s = int(x) + int(y)
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{x}').click()
    driver.find_element_by_id('com.android.calculator2:id/op_add').click()
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{y}').click()
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    # 获取实际结果 com.android.calculator2:id/formula
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text
    if int(result) == s:
        print(f"{x}+{y}={s},测试通过")
    else:
        print(f"{x}+{y}={s},测试失败")
sleep(2)
driver.quit()
"""

# 3.文件的操作

# 3.1 csv文件的处理
# table = CsvUtil().read_all_csv('login.csv')
# for item in table:
#     print(item)

# 3.2 yaml文件的处理
# yaml = YamlUtil().read_all_yaml('data_list\\Pm_Login_list.yaml')
# for item in yaml:
#     print(item)

"""
# 4.模拟器执行的程序:（通过文件传入数据）
table = CsvUtil().read_all_csv('login.csv')
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
caps['deviceName'] = "192.168.110.101:5555"  # 测试手机的名称
caps['appPackage'] = "com.android.calculator2"  # 被测app的包名
caps['appActivity'] = '.Calculator'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
for item in table:
    # s = int(item[0]) + int(item[1])
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{item[0]}').click()
    driver.find_element_by_id('com.android.calculator2:id/op_add').click()
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{item[1]}').click()
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    # 获取实际结果 com.android.calculator2:id/formula
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text
    if int(result) == int(item[2]):
        print(f"{item[0]}+{item[1]}={item[2]},测试通过")
    else:
        print(f"{item[0]}+{item[1]}={item[2]},测试失败")
sleep(2)
driver.quit()
"""

# 3.3 文件的写入
"""
rows = CsvUtil().read_all_csv("test1.csv")
# 创建一个新的测试报告文件
file2 = open("test2.csv", "w", newline="")  # newline去掉空行
writer = csv.writer(file2)
# 写入测试数据+测试结论
for row in rows:
    row.append("测试通过")
    writer.writerow(row)  # 行之间元素用逗号隔开
file2.close()
"""

"""
rows = CsvUtil().read_all_csv("test1.csv")
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
caps['deviceName'] = "192.168.110.101:5555"  # 测试手机的名称
caps['appPackage'] = "com.android.calculator2"  # 被测app的包名
caps['appActivity'] = '.Calculator'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)

file2 = open("test2.csv", "w", newline="")  # newline去掉空行
writer = csv.writer(file2)
for item in rows:
    # s = int(item[0]) + int(item[1])
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{item[0]}').click()
    driver.find_element_by_id('com.android.calculator2:id/op_add').click()
    driver.find_element_by_id(f'com.android.calculator2:id/digit_{item[1]}').click()
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    # 获取实际结果 com.android.calculator2:id/formula
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text
    if int(result) == int(item[2]):
        # print(f"{item[0]}+{item[1]}={item[2]},测试通过")
        item.append("测试通过")
        writer.writerow(item)
    else:
        item.append("测试失败")
        writer.writerow(item)
        # print(f"{item[0]}+{item[1]}={item[2]},测试失败")
file2.close()
sleep(2)
driver.quit()
"""
table = CsvUtil().read_all_csv("test_zh.csv")
file2 = open("test3.csv", "w", newline="")
writer = csv.writer(file2)
caps = {}
caps['automationName'] = "UiAutomator2"
caps['platformName'] = "Android"  # 声明被测手机系统是ios还是Android
caps['platformVersion'] = '6.0'  # 测试手机的Android版本号
caps['deviceName'] = "192.168.110.101:5555"  # 测试手机的名称
caps['appPackage'] = "com.android.calculator2"  # 被测app的包名
caps['appActivity'] = '.Calculator'
driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
for item in table:
    driver.find_element_by_id('com.android.calculator2:id/formula').send_keys(f"{item[0]+item[1]+item[2]+item[3]+item[4]}")
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text

    # 出现了上一个的结果拼接上了下一个数据
    if result == item[5]:
        # print(f"{item[0]}+{item[1]}={item[2]},测试通过")
        item.append(f"{item[0]+item[1]+item[2]+item[3]+item[4]}={item[5]}测试通过")
        writer.writerow(item)
    else:
        item.append(f"{item[0]+item[1]+item[2]+item[3]+item[4]}={item[5]}测试失败")
        writer.writerow(item)
        # print(f"{item[0]}+{item[1]}={item[2]},测试失败")
    el = driver.find_element_by_id("com.android.calculator2:id/clr")
    TouchAction(driver).long_press(el).perform().wait(3000)
    driver.find_element_by_id("com.android.calculator2:id/clr").click()
file2.close()
sleep(2)
driver.quit()

