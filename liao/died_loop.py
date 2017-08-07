# --coding: utf-8--
# 2017/8/7

'写一个死循环监测cpu占用情况'

import threading, multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()