# coding=utf-8

__author__ = 'Darcy'

import requests
import re

# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
# 修改http头
# headers = {'User-Agent':'此处待添加'}
# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers = headers)

html = requests.get('http://www.qqjay.com/yijingtupian/86114.html')
html.encoding = 'utf-8'

image_list = re.findall('http:.*?.jpg', html.text)

i = 0

# 爬取网页图片
for each in image_list:
    img = open(r'/Users/zhang/imgs/scenery/' + str(i) + '.jpg', 'wb')
    response = requests.get(each)
    buf = response.content
    img.write(buf)
    i += 1


print html.text
