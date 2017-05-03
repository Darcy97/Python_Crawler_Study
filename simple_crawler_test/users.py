# coding=utf-8

__author__ = 'Darcy'

import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt', 'r')
html = f.read()
f.close()

# # 爬取标题
# title = re.search('<title>(.*?)</title>', html, re.S).group(1)
# print title
# # 爬取链接
# links = re.findall('href="(.*?)"', html, re.S)
# for each in links:
#     print each

# 爬取部分文本，先大再小
# text_field = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
# print text_field
# the_text = re.findall('">(.*?)</a>', text_field, re.S)
# for item in the_text:
#     print item

# sub 实现翻页
for i in range(2, total_page + 1):
    new_link = re.sub('pageNum=(\d+)', 'pageNum=%d'%i, old_url)
    print new_link
