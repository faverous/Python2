# --coding: utf-8--
# 2017/8/7

'多线程之间的变量是共享的，所以要注意多线程之间的数据变化'

import time, threading

# 银行存款
balance = 0
lock = threading.Lock()	#创建锁实例

def change_it(n):
	# 先存后取，balance应该为0
	global balance	# global关键字，规定变量作用在整个程序中，默认变量是内部变量
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		lock.acquire()	#获取锁
		try:
			change_it(n)
		finally:
			lock.release()	#关闭锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance