# --coding: utf-8--
# 面向对象高级编程，动态的给实例绑定属性或方法
# 2017/8/4

from types import MethodType

# 定义一个不含方法和属性的类
class Student(object):
	pass

# 动态属性
s = Student()
s.name = 'Tom'
print s.name

# 动态方法
def set_age(self, age):
	self.age = age

# 给s实例绑定一个方法
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age
# 这种方法绑定的方法只能应用在这个实例上，新的实例不能使用
s2 = Student()
# s2.set_age(20)
# print s2.age

# 给Student类动态的绑定上方法，相当于静态定义类时设定的方法
Student.set_age = MethodType(set_age, None, Student)

s2.set_age(22)
print s2.age

# 测试这样的Student类是否可以继承
class Mine(Student):
	pass

s3 = Mine()
s3.set_age(34)
print s3.age
#测试通过，可以继承