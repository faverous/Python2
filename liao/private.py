# -- coding: utf-8 --
# 2017/08/03
# 内部属性

class Student(object):

	def __init__(self, name, score):
		self.__name =  name #__+变量名表示该变量是内部变量，在外部无法访问
		self.__score = score

	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)

	def get_name(self):
		return self.__name

#  错误输出	
bart = Student('Tom', 100)
#print bart.__name

#  正确输出
#  给Student类增加get方法，获取数据
print bart.get_name()