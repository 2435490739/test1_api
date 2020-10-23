# coding=utf-8

import os
import yaml

cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName):
    p = os.path.join(cur, yamlName)
    file1 = open(p)
    a = file1.read()
    t = yaml.load(a, Loader=yaml.FullLoader)  # 通过load函数转化为字典或者列表的形式
    #print t
    file1.close()
    #print type(t['token'])
    if t is not None:
        token = str(t['token'])
        return token
    else:
        print ("请先登录!")



if __name__=="__main__":
    print get_token("token.yaml")