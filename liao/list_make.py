# --coding: utf-8--
# 列表生成器
# 20170728
L = []
print "利用循环"
for x in range(1,11):
	L.append(x * x)
print L

print "利用内置生成器"
M = [x * x for x in range(1,11)]
print M
