# coding=utf-8

__author__ = 'Darcy'

import re

# 正则表达式的使用
# # .
# a = "sx123"
# b = re.findall('x.', a)
#
# print b


# # *
# a = 'xexe234'
# b = re.findall('x*', a)
# print b


# # ?
# a = 'x3zx23'
# b = re.findall('x?', a)
# print b

secret_code = 'SHAJFAKJSFxxHelloxx2323xxworldxx'

# # .*
# b = re.findall('xx.*xx', secret_code)
# print b
#
# # .*?
# b = re.findall('xx.*?xx', secret_code)
# print b
#
# (.*?)
# b = re.findall('xx(.*?)xx', secret_code)
# print b
# for each in b:
#     print each
#
#
# (.*?)
# s2 = 'asdfxxixx123xxlovexxdfsxxsecondxx123xxphrxxtuyty'
# result = re.findall('xx(.*?)xx123xx(.*?)xx', s2)
# print result[1][1]
#
# # 换行
# s = '''asdfasdxxhello
# xx234sdfxxworldxx'''
#
# b = re.findall('xx(.*?)xx', s, re.S)


# 对比findall 与 search
# s = 'sfsdxxIxxsdfsxxlovexxsdfsxxyouxx'
# d = re.search('xx(.*?)xxsdfsxx(.*?)xx', s).group(2)
# print d


# 匹配数字
# s = 'sfas32424zfsd342'
# result = re.findall('(\d+)', s)
# print  result


# sub
# s = 'werq123sfsdfsf123qwerwq'
# b = re.sub('123(.*?)123', '12222%d123'%789, s)
# print b
