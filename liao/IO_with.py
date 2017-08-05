# --coding: utf-8--
# 2017/8/5

'利用python自带的with方法，可以更便捷的实现file的IO'

def file_read():
	with open('test.txt','r') as f:
		print f.read()
	return f

file_read()
print '123'