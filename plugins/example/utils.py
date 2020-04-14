# -*- coding: UTF-8 -*-

import requests
import twint

def get_content():
    url = 'http://open.iciba.com/dsapi/'
    res = requests.get(url)
    content_e = res.json()['content']
    content_c = res.json()['note']
    return [content_c, content_e]
