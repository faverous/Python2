# --coding:utf-8--
# 2017/8/5

'查找当前目录下文件名中包含某字符串所有文件'
import os
from sys import argv
script, string = argv

print '包含%s字符串的文件如下：' % string

'获取当前目录'

path_fir = os.path.abspath('.')

def search(path_fir, string):
	for x in os.listdir('.') :
		if os.path.isfile(x):
			if os.path.splitext(x)[0]==string:
				print x
			else:
				print '%s文件夹下无该文件！' % path_fir
		else:
			path_fir = os.path.join('path_fir', x)
			search(path_fir, string)
			

def main():
	search(path_fir, string)

main()