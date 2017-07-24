# -- coding:utf-8 --
from sys import argv
script, filename = argv #第二个参数为文件名
txt = open(filename,"w") #读取文件
print "Here's your file %r:" % filename
txt.truncate() #读取文件并打印
txt.close()
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()