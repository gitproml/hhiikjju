# -*- coding: utf-8 -*-
# @Time    : 2023/5/12 10:28
# @Author  : muyangren907
# @Email   : myr907097904@gmail.com
# @File    : renderyaml.py
# @Software: PyCharm
import yaml
import os
import random


def get_yaml_data(yaml_file):
    # 打开yaml文件
    # print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # print(file_data)
    # print("类型：", type(file_data))

    # # 将字符串转化为字典或列表
    # print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    # print(data)
    # print("类型：", type(data))
    return data


def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def gendic(aaa):
    rint1 = random.randint(7, 12)
    rstr1 = generate_random_str(rint1)

    retdic = {
        'type': 'web',
        'name': '{}'.format(rstr1),
        'env': 'docker',
        'repo': None,
        'region': 'singapore',
        'plan': 'free',
        'branch': 'main',
        'rootDir': '{}'.format(aaa),
        'dockerCommand': None,
        'numInstances': None,
        'healthCheckPath': '/',
        'autoDeploy': False
    }
    return rstr1, retdic


if __name__ == '__main__':
    # current_path = os.path.abspath(".")
    # yaml_path = os.path.join(current_path, "renderbak.yaml")
    # yamldic = get_yaml_data(yaml_path)

    # print(yamldic)

    dirstr = ''
    with open("dir.ini", mode='r', encoding='utf-8') as dirini:
        dirstr = dirini.read()
    serviceslist = []
    retslit = []
    for iii in dirstr.split('\n'):
        if ' && ' in iii:
            aaa, bbb = iii.split(" && ")
            aaa = aaa.split(' ')[1]
            bbb = bbb.split(" ")[2].replace('"', '')
            # print(aaa, bbb)
            rstr1, retdic11 = gendic(aaa)
            serviceslist.append(retdic11)
            retslit.append(rstr1)

    with open('ret.txt', mode='w', encoding='utf-8') as rettx:
        for iiii in retslit:
            rettx.write('{}\n'.format(iiii))

    fdnum = 10

    fidx = 0
    yamlidx = 0
    serviceslist1 = []
    for iii in serviceslist:
        serviceslist1.append(iii)
        fidx += 1
        if fidx == 10:
            fidx = 0
            retdic = {
                'services': serviceslist1
            }
            curpath = os.path.dirname(os.path.realpath(__file__))
            yamlidx += 1
            yamlpath = os.path.join(curpath, "render{}.yaml".format(yamlidx))

            # 写入到yaml文件
            with open(yamlpath, "w", encoding="utf-8") as f:
                yaml.dump(retdic, f)
    retdic = {
        'services': serviceslist1
    }
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlidx += 1
    yamlpath = os.path.join(curpath, "render{}.yaml".format(yamlidx))

    # 写入到yaml文件
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(retdic, f)

    # print(retdic)
