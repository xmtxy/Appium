# @pytest.mark.parametrize �� yaml ��ϵĴ�����:

import json
from common.yaml_util import YamlUtil
import os
import yaml


# ��ȡ��������(��Ϊ��Ҫ�����ݽ��н�һ���Ĵ���....
def read_testcase(yaml_name):
    base_path = os.getcwd() + '\\test_case\\' + yaml_name
    with open(base_path, mode='r', encoding='utf-8') as f:
        caseinfo = yaml.load(f, yaml.FullLoader)
        # print(caseinfo,len(caseinfo)) # [{"name":"$ddt{name},...."}] 1
        # print(dict(*caseinfo).keys()) # ['name', 'parameterize', 'request', 'extract', 'validate']
        # print(*caseinfo) # {"name":"$ddt{name},...."}
        if len(caseinfo) >= 2:  # �ж�yaml�����ļ����м�������,���������ڵ���2ʱ,ֱ�ӷ���caseinfo === ������������
            return caseinfo
        else:  # ������1ʱ,��Ϊ�����������caseinfo���ֵ��б����Ǿ���Ҫ��caseinfo���
            if "parameterize" in dict(*caseinfo).keys():  # ת�����ֵ�
                new_caseinfo = ddt(*caseinfo)  # ��������ķ���
                # print(new_caseinfo)
                return new_caseinfo
            elif "datas" in dict(*caseinfo).keys():
                new_caseinfo = step(*caseinfo)  # ��������ķ���
                return new_caseinfo
            else:
                return caseinfo


def ddt(caseinfo):  # �����ֵ�Ǽ���{"name":"$ddt{name}",......}
    if "parameterize" in caseinfo.keys(): # {'name', 'parameterize', 'request', 'extract', 'validate'}
        caseinfo_str = json.dumps(caseinfo)  # �ж�parameterize�Ƿ���caseinfo��,����ԭ����
        print(caseinfo_str)  # {"name":"$ddt{name}",......}
        # for ѭ������ �õ�ÿһ�Ե�()
        for param_key, param_value in caseinfo["parameterize"].items(): # d.items()�����ֵ��е����м�ֵ����Ϣ [(),(),...]
            # print(caseinfo["parameterize"].items()) # dict_items([('name-username-password-project-assert_str', '/datas/Pm_Login_List.yaml')])
            key_list = param_key.split("-")  # ��param_keyת���б� # ���ǽ� name-username-password-project-assert_str ת�����б�
            data_list = YamlUtil().read_all_yaml(param_value)  # ��ȡparam_value
            # print(data_list) # [[], [],...]
            # �淶yaml�����ļ���д��(��һ�¾��˳�ִ��
            length_flag = True
            # for ѭ������
            for data in data_list:
                if len(data) != len(key_list):
                    length_flag = False
                    break
            # �滻ֵ( length_flag = True ��ִ�е��߼�....
            new_caseinfo = []
            if length_flag:
                for x in range(1, len(data_list)):  # ѭ�����ݵ����� 1,2,3,4  === �������ݵ�����
                    # print(x)
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(data_list[x])):  # ѭ��������-��ȡֵ 0,1,2,3,4  === ÿһ���������ݵ�Ԫ�ظ���
                        # print(y)
                        if data_list[0][y] in key_list:  #[['name', 'username', 'password', 'project', 'assert_str'],[],..] ÿһ��ֵѭ��һ��,������Ҫ����㶼ѭ��
                            # �滻ԭʼ��yaml����� $ddt{xxx}
                            # a = 2 isinstance(a,int) # ������� True
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                      str(data_list[x][y]))
                            else:
                                temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                      str(data_list[x][y]))  # ��1��ʼ,Ҳ���ǵڶ�����������ȥȡ����
                    new_caseinfo.append(json.loads(temp_caseinfo))

        # print(new_caseinfo)  # [{'name':'xxx',......}]
        # print(type(new_caseinfo)) # list
        return new_caseinfo
    else:
        return caseinfo

def step(caseinfo):
    if "datas" in caseinfo.keys():
        caseinfo_str = json.dumps(caseinfo)  # �ж�datas�Ƿ���caseinfo��,����ԭ����
        # print(caseinfo_str)
        # for ѭ������ �õ�ÿһ�Ե�()
        for param_key, param_value in caseinfo["datas"].items():  # d.items()�����ֵ��е����м�ֵ����Ϣ [(),(),...]
            key_list = param_key.split("-")  # ��param_keyת���б� # ���ǽ� one-two-three-four-five-six-seven-eight-nine-ten ת�����б�
            data_list = YamlUtil().read_all_yaml(param_value)  # ��ȡparam_value
            # print(key_list)
            # print(data_list)  # [[....], ['������ȷ�˺�', '������ȷ����', '�����¼'],...]
            # �淶yaml�����ļ���д��(��һ�¾��˳�ִ��
            length_flag = True
            # for ѭ������
            """
            for data in data_list:
                if len(data) != len(key_list):
                    print(len(data))
                    data.append(' ')
                    print(len(data))
                    print(len(key_list))
                    length_flag = False
                    break
                print(data)  # ['one',...][][][]...
            """
            for data in data_list:
                for i in range(len(key_list)-len(data)):
                    data.append('None')
            # �滻ֵ( length_flag = True ��ִ�е��߼�....
            new_caseinfo = []
            if length_flag:
                for x in range(1, len(data_list)):  # ѭ�����ݵ����� 1,2,3,4  === �������ݵ�����
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(data_list[x])):  # ѭ��������-��ȡֵ 0,1,2,3,4  === ÿһ���������ݵ�Ԫ�ظ���
                        # print(key_list)['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
                        if data_list[0][y] in key_list:  # ÿһ��ֵѭ��һ��,������Ҫ����㶼ѭ��
                            # �滻ԭʼ��yaml����� $ddt{xxx}
                            # a = 2 isinstance(a,int) # ������� True
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$step{' + data_list[0][y] + '}"',
                                                                      str(data_list[x][y]))
                            else:
                                print(data_list[x][y])
                                temp_caseinfo = temp_caseinfo.replace("$step{" + data_list[0][y] + "}",
                                                                      str(data_list[x][y]))  # ��1��ʼ,Ҳ���ǵڶ�����������ȥȡ����

                    new_caseinfo.append(json.loads(temp_caseinfo))

            # print(new_caseinfo) # [{'name':'xxx',......}]
            # print(type(new_caseinfo)) # list
        return new_caseinfo
    else:
        return caseinfo
