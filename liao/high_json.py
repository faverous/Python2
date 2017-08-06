# --coding: utf-8--
# 2017/8/6

'将类转化成json'
import json

class Student(object):
	def __init__(self, name, score, age):
		self.name = name
		self.score = score
		self.age = age

'定义一个将类转化成dict的方法'
'''
def trans(std):
	return {
		'name': std.name,
		'score': std.score,
		'age': std.age
	}
'''

s = Student('Bob', 20, 88)
#print(json.dumps(s, default=trans))
'偷懒的通用方法，适用于所有类'
print(json.dumps(s, default= lambda obj: obj.__dict__))
