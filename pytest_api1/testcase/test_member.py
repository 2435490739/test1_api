# coding=utf-8

import requests
import yaml
import json
from common.re_token import get_token

def get_test_data(test_data_path):
    case = []
    http = []
    expected = []
    file1 = open(test_data_path)
    a = file1.read()
    dat = yaml.load(a, Loader=yaml.FullLoader)
    file1.close()
    test = dat['tests']
    #print test
    for td in test:
        case.append(td.get('case', ''))
        http.append(td.get('http', {}))
        expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return parameters

test_data_path1 = '/Users/apple/PycharmProjects/pythonProject1/pytest_api/data/test_member.yaml'


class TestMember(object):
    def test_member(self):
        parameters = get_test_data(test_data_path=test_data_path1)
        print parameters
        list_params = list(parameters)
        print list_params
        host = 'http://luxury-mall-dev.ssluxury.cn'
        path = list_params[0][1]['path']
        print path
        data = list_params[0][1]["data"]
        headers = list_params[0][1]["headers"]
        token = get_token("token.yaml")
        print token
        r = requests.post(url=host+path, data=json.dumps(data), headers=headers)
        print r.text



if __name__=="__main__":
    TestMember().test_member()





