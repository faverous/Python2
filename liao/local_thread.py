# --coding: utf-8--
# 2017/8/7

'利用ThreadLocal对象，可以创建一个全局对象，而他的各个属性在线程之间又是相互独立的'

import threading

local_school = threading.local()

def process_student():
	print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target=process_thread, args=('Tom',))
t2 = threading.Thread(target=process_thread, args=('Mike',))
t1.start()
t2.start()
t1.join()
t2.join()

