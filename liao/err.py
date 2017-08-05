# --coding: utf-8--
# 2017/8/5

'未被捕获的错误会一直上抛，最终被Python解释器捕获'
'''
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

main()
'''

'定义异常抛出'
class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo('0')