# coding=utf-8
import requests
import json


def test_add_address():
    host = 'http://luxury-mall-dev.ssluxury.cn'
    path = '/api-u/address/save'
    data = {
    "address": "1号",
    "areaId": 1203,
    "areaName": "西湖区",
    "cityId": 119,
    "cityName": "杭州市",
    "isDefault": "",
    "mobile": "18296637289",
    "name": "green",
    "provinceId": 11,
    "provinceName": "浙江省",
    "townId": 15070,
    "townName": "文新街道"
    }

    token ='eyJleHBpcmVfdGltZSI6MTYwMzg3NTUwMzgxMiwibG9naW5fdGltZSI6MTYwMzI3MDcwMzgxMiwidXNlciI6eyJhcHAiOjUsImNyZWF0ZV90aW1lIjoxNTk4OTU1NDE5MDAwLCJpZCI6MTMwMDczOTQyMDY4MTk5NDI0MSwicGhvbmUiOiIxODI5NjYzNzI4NSIsInByaXZpbGVnZSI6IjAifSwic2lnbiI6IjEzZDVkZjA4YTI0ZDE1ZjAzMDEwMDNjZWQ3ZDM4MjA1MTY4Y2IxYTZiMjg0OTA4MjRjYWYyMzYwNmE5MTM2ZTYifQ=='
    headers = {"Content-Type": "application/json", "x-shop-token": token}
    r = requests.post(url=host + path, data=json.dumps(data), headers=headers)
    print r.text
    return r.text

if __name__=="__main__":
    test_add_address()