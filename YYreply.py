# coding: utf-8
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def Tuling(words):
    Tuling_API_KEY = "98d3f9a8323446eda959fc0d7dfb3c4a"#此处填写自己的Turling KEY

    body = {"key":Tuling_API_KEY,"info":words.encode("utf-8")}

    url = "http://www.tuling123.com/openapi/api"
    r = requests.post(url,data=body,verify=True)

    if r:
        date = json.loads(r.text)
        print date["text"]
        return date["text"]
    else:
        return None