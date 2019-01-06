#coding=utf-8

import logging
from bs4 import BeautifulSoup
import requests
import re
import time

# 尝试搜索网页
class mSoup:
    def __init__(self, url=None):
        self.url = url
        self.content = ""
        pass

    # 获取网页内容 - 会尝试重连10次
    def parseHtml(self):
        for i in range(0, 10):
            try:
                c = requests.get(self.url)
                if c.status_code != 200:
                    time.sleep(1)
                else:
                    self.content = c.text
                    break
            except Exception as e:
                logging.debug("error is %s" % str(e))

        if self.content == "":
            logging.debug("请求异常！")
        pass

    # 获取内容
    def getContent(self, name, attrs):
        self.parseHtml()

        if self.content:
            soup = BeautifulSoup(self.content)
            return soup.find_all(name=name, attrs=attrs)
        pass

# s = mSoup('https://www.python.org/downloads/windows/')
# a_list = s.getContent(name="a", attrs={"href": re.compile("/community/")})
# for x in a_list:
#     print(x)