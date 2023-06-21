import os
from time import sleep

import pytest


if __name__ == '__main__':
    pytest.main()
    sleep(3)  # 让它先生成临时文件
    split = 'allure ' + 'generate ' + './report/temporary ' + '-o ' + './report/html ' + '--clean'
    os.system(split)  # 调用dos命令
    