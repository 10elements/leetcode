a = 0

def fun1():
	# global a
	a = a + 1

def fun2():
	print(a)
	
fun1()
fun2()
print(a)