# coding=utf-8

import requests
import json
import yaml
import os


cur = os.path.dirname(os.path.realpath(__file__))

def login():
    headers = {"Content-Type": "application/json"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    #print r.text
    print r.json()['data']['token']
    a = r.json()['data']['token']
    return a


def write_yaml():
    token = login()
    t = {'token': token}
    curl1 = os.path.join(cur, 'token.yaml')
    print curl1
    with open(curl1, "w") as f:
        yaml.dump(t, f)



if __name__=="__main__":
   write_yaml()