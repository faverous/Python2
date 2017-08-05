# --coding:utf-8--
# 错误处理机制
# 2017/8/5

try:
	print 'try...'
	r = 10 / 5
	print 'result:', r
except BaseException, e:
	print 'except:', e
else:
	print 'No Error'
finally:
	print 'finally...'
print 'END'