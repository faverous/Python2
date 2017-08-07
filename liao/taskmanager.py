# --coding: utf-8--
# 2017/8/7

'分布式进程，服务器端'

import random, time, Queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = Queue.Queue()
# 接收结果的队列
result_queue = Queue.Queue()

class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000，设置验证码‘abc’
manager = QueueManager(address=('', 5000), authkey='abc')
manager.start()	# 启动queue
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放入任务
for i in range(10):
	n = random.randint(0, 10000)
	print 'Put task %d...' % n
	task.put(n)
# 从result队列读取结果
print 'Try get results...'
for i in range(10):
	r = result.get(timeout=10)
	print 'Result: %s' % r
# 关闭
manager.shutdown()