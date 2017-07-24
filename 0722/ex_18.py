# --coding: utf-8 --
# --函数的使用--
# --定义函数--
def print_two(* args):  # 指针类型，动态接受参数
	arg1, arg2, arg3 = args #解包，将参数内容分解开，存给定义的变量
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothing."

# --调用函数--
print_two("Zed","Tom","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
