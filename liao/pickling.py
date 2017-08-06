# --coding: utf-8--
# 2017/8/6

'序列化'
import pickle

def save(m):
	try:
		f = open('pick.txt','wb')
		pickle.dump(m, f)
		print '保存成功'
	except StandardError, e:
		print 'except: ', e
	finally:
		f.close()

def load():
	try:
		f = open('pick.txt', 'rb')
		m = pickle.load(f)
		print '读取成功'
		return m
	except StandardError, e:
		print 'Except:', e
	finally:
		f.close()

def main():
	d = {'name': 'mj', 'score': 100}
	g = raw_input()
	save(g)
	m = load()
	print m

main()