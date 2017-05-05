# coding=utf-8

__author__ = 'Darcy'

import re
import urllib2


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
# for i in range(2, total_page + 1):
#     new_link = re.sub('pageNum=(\d+)', 'pageNum=%d'%i, old_url)
#     print new_link

# 爬取代码文本

cpu_f = open('cpu_design.html', 'r')
cpu_html = cpu_f.read()
cpu_f.close()

print '\n'
code_list = re.findall('<pre><code>(.*?)</code></pre>', cpu_html, re.S)

test_text = open('test_text', 'w')

for item in code_list:
    test_text.write(item)
    test_text.write('\n\n\n\n')


