# --coding: utf-8--
# 2017/8/7

'实现多任务时，可以利用一个进程多个线程实现'

import time, threading

# 新线程执行的代码
def loop():
	print 'thread %s is running...' % threading.current_thread().name
	n = 0
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s' % (threading.current_thread().name, n)
		time.sleep(5)	#延迟时间（s）
	print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop)
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name