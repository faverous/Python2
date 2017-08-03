#--coding:utf-8--
#多态的使用
#2017/8/3

class animal(object):
	def run(self):
		print 'animal is running...'

class dog(animal):
	def run(self):
		print 'dog is running...'
	def eat(self):
		print 'dog is eating...'

class cat(animal):
	def run(self):
		print 'cat is running...'

def run_twice(animal):
	animal.run();

run_twice(animal())
run_twice(dog())
run_twice(cat())