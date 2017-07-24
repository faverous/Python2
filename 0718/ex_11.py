#-- coding: utf-8 --
print "How old are you?",
age = raw_input()
print "How tall are you?"   #没有逗号会导致输入的内容换行输入
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So, you are %r old, %r tall, %r weight" % (age,height,weight)