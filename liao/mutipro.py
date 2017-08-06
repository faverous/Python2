# --coding: utf-8--
# 2017/8/6

'跨平台的进程创建'

from multiprocessing import Process
import os

# 子进程要调用的方法
def child_run(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':	#__name__表示当前模块的名字，这句话的作用是，当直接调用该py文件时，执行下面的代码，当作为模块引入时，不执行
	print 'Parent process %s.' % os.getpid()
	p = Process(target=child_run, args=('name',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end.'
