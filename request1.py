# coding=utf-8

import requests
import json
import logging

s = requests.session()

url = 'http://luxury-mall-dev.ssluxury.cn/api-u/user/phonePasswordNoCode'
data = {"phone": "18296637285", "password": "a123456"}
headers = {"Content-Type": "application/json"}

r =s.post(url=url,data=json.dumps(data),headers=headers)
print r.text
logging.info("登录成功")