# --coding: utf-8--
# 使用@property将方法绑定成属性，防止属性直接暴露，同时可以给属性添加限制条件
# 2017/8/4

# 假设Student类有score属性，score只能时int型，且规定范围在0-100
# 一般方法实现
'''
class Student(object):

	def get_score(self):
		return self.score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be a integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self.score = value

s = Student()
s.set_score(60)
print s.get_score()
s.set_score(999)
'''

# @property装饰器实现
class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be a integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value

s = Student()
s.score = 60
print s.score
s.score = 'hmj'