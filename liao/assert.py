# --coding: utf-8--
# 2017/8/5

'assert断言的使用'

main()

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero'   #assert后面的语句应该为True，否则报错
	return 10 / n

def main():
	foo('0')

