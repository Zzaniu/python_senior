#coding=utf-8

# 乱码无法解决，放弃

import json
import requests

def getWeather(city):
    r = requests.get("http://www.weather.com.cn/data/cityinfo/101010100.html")
    print r.json()['data']

r = requests.get("http://www.weather.com.cn/data/cityinfo/101010100.html")
print r.json()