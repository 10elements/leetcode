def sort(stack):
	if len(stack):
		tmpStack = []#sorted in descending order
		size = len(stack)
		for i in range(size):
			top = stack.pop()
			cnt = 0
			while len(tmpStack) and tmpStack[-1] > top:# find the right place to insert top into tmpStack
				stack.append(tmpStack.pop())#move elements larger than top to stack
				cnt += 1
			tmpStack.append(top)#insert top into the right place on tmpStack
			for i in range(cnt):# move those elements larger than top back to tmpStack
				tmpStack.append(stack.pop())
		while len(tmpStack):
			stack.append(tmpStack.pop())

def main():
	stack = [1, 1, 8, 0, 7, 10, 2]
	sort(stack)
	print(stack)

if __name__ == '__main__':
	main()
