# -*- coding: utf-8 -*-
import requests
import urllib
import json
#url = "http://fanyi.youdao.com/"
def translate(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data = {}
    data["action"] = "FY_BY_REALTIME"
    data["client"] = "fanyideskweb"
    data["doctype"] = "json"
    data["from"] = "AUTO"
    data["i"] = content
    data["keyfrom"] = "fanyi.web"
    data["smartresult"] = "dict"
    data["to"] = "AUTO"
    data["typoResult"] = "false"
    data = urllib.urlencode(data)
    response = urllib.urlopen(url, data)
    html = response.read()
    target = json.loads(html)
    result = target["translateResult"][0][0]['tgt']
    return result

