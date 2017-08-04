# --coding: utf-8--
# 多重继承Mixin
# 2017/8/4

'首先设计两个大类，让子类继承，再设计两个类，可以让子类同时继承两个大类'

class Animal(object):
	pass

class Bird(Animal):
	def echo(self, name):
		print '%s is a Bird...' % name

class Parrot(Bird):
	pass

parrot = Parrot()
parrot.echo('parrot')

class FlyableMixin(object):
	def fly(self):
		print 'I\'m flying...'

class A(Bird, FlyableMixin):
	pass

a = A()
a.echo('a')
a.fly()