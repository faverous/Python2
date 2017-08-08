# --coding: utf-8--
# 2017/8/8

'python中提供了re模块，提供所有正则表达式功能'

import re

a = 'abc-001'	#第一个\是转义字符，‘abc\-001’
b = r'abc\-001'		#通过r前缀，可以忽略python的\转义功能
if re.match(b, a):
	print 'ok'
else:
	print 'failed'

def email(address):
	ex = '^[0-9a-zA-Z_]+@[a-zA-Z]+(\.[a-z]+)+$'
	if re.match(ex, address):
		print 'ok1'
	else:
		print 'failed'

if __name__=='__main__':
	inp = raw_input()
	email(inp)

