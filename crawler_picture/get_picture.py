# coding=utf-8

__author__ = 'Darcy'

import urllib2
import re

url = 'http://www.ivsky.com/tupian/ertong_huanxiang_feixingyuan_v41125/'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
content = response.read()

# print content


list_url = re.findall('http:.*?jpg', content)
print list_url

i = 0
for url in list_url:

     f = open(r"/Users/zhang/imgs"+'/'+str(i)+'.jpg', 'wb')
     print url
     req = urllib2.urlopen(url)
     buf = req.read()
     f.write(buf)
     i += 1

