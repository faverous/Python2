# --coding: utf-8--
# 20170728
# 列表切片练习
L = range(100)
print L

print "前10个数"
print L[:10]

print "后10个数"
print L[-10:]

print "前11-20个数"
print L[10:20]

print "前10个数，每两个取一个"
print L[:10:2]

print "复制整个列表"
M = L[:]
print "M:", M
