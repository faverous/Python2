# -- coding: utf-8 --
# 继承和多态的使用
# 2017/08/03

# 构造父类
class Animal(object):
	def run(self):
		print 'Animal is running...'

# --dog和cat便是Animal的子类，继承了Animal的所有方法--
class dog(Animal):
	def run(self):
		print 'Dog is running...'

class cat(Animal):
	def run(self):
		print 'Cat is running...'

dog = dog()
dog.run()

Cat = cat()
Cat.run()