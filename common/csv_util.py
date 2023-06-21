import os  # 处理路径的问题

import csv  # csv文件包

# class CsvUtil:
#     def read_all_csv(self, base_path):
#         # os.getcwd() 获得目录的当前系统程序工作路径
#         # print(os.getcwd()+"/extract.yaml") #D:\PythonPc_App\Appium基础\common
#         # print(os.getcwd().replace('Scratch', 'data_list\\')+base_path)
#         with open(os.getcwd().replace('Scratch', 'data_list\\')+base_path, encoding="utf-8") as file:
#             value = csv.reader(file)
#             for item in value:
#                 print(f"{item}")
#             # return value
# 读取Excel文件的方法(优化)--可用于注册登录等等表格的读取


class CsvUtil:
    def read_all_csv(self, filename):
        # path="../test_data/"+filename
        # 多个.py文件的测试用例如何一起执行时,会出现路径查找不到的情况
        base_path = os.path.dirname(__file__)  # 获取当前文件的路径的地址,而不是相对主函数
        # print(base_path) D:\PythonPc_App\SeleniumTest\function
        path = base_path.replace("common", "data_list/"+filename)  # replace替换到想要的文件路径
        # print(path) D:\PythonPc_App\Appium基础\data_list/login.csv
        list = []
        # f=open(path,'r',encoding="utf-8-sig")
        # 优化忘记关闭文件的操作
        with open(path, 'r', encoding="utf-8-sig") as f:
            table = csv.reader(f)  # 读取数据
            # 出现了调用第一行数据,如何解决?
            # list = []
            i = 0
            for item in table:
                if i == 0:
                    pass
                else:
                    list.append(item)
                i += 1
            return list
