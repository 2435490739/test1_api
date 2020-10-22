# coding=utf-8

import requests
import pytest
import json


class TestAddress(object):
    def test_member(self):
        host = 'http://luxury-mall-dev.ssluxury.cn'
        path = '/api-u/user/detail'
        data = {}
        token = 'eyJleHBpcmVfdGltZSI6MTYwMzg3NTUwMzgxMiwibG9naW5fdGltZSI6MTYwMzI3MDcwMzgxMiwidXNlciI6eyJhcHAiOjUsImNyZWF0ZV90aW1lIjoxNTk4OTU1NDE5MDAwLCJpZCI6MTMwMDczOTQyMDY4MTk5NDI0MSwicGhvbmUiOiIxODI5NjYzNzI4NSIsInByaXZpbGVnZSI6IjAifSwic2lnbiI6IjEzZDVkZjA4YTI0ZDE1ZjAzMDEwMDNjZWQ3ZDM4MjA1MTY4Y2IxYTZiMjg0OTA4MjRjYWYyMzYwNmE5MTM2ZTYifQ=='
        headers = {"Content-Type": "application/json", "x-shop-token": token}
        reponse1 = requests.post(url=host + path, data=data, headers=headers)
        print reponse1.text
        r = reponse1.json()
        print r['data']['userInfo']['mobile']
        r1 = r['data']['userInfo']['mobile']
        print type(r1)
        r1 = int(r1)
        print type(r1)
        assert r1 == 18296637285


if __name__=="__main__":
    pytest.main(['-s', 'test_add_address.py'])
