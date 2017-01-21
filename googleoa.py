def solution1(X):
	maxNum = 0
	num = str(X)
	for i in range(len(num) - 1):
		if num[i] == num[i + 1]:
			maxNum = max(maxNum, int(num[:i] + num[i + 1:]))
	return maxNum

def solution2(X):
	minNum = float('inf')
	num = str(X)
	for i in range(len(num) - 1):
		if num[i] >= num[i + 1]:
			minNum = min(minNum, int(num[:i + 1] + num[i + 2:]))
		else:
			minNum = min(minNum, int(num[:i] + num[i + 1:]))
	return minNum

def solution3(X):
	maxNum = 0
	num = str(X)
	l = len(num)
	for i in range(l - 1):
		maxNum = max(maxNum, int(num[:i] + str(int((int(num[i]) + int(num[i + 1])) / 2 + 1)) + num[i + 2: ]))
	return maxNum

def pathSearch(paths):
	totallgth = 0
	paths = paths.split('\n')
	stack = [paths[0]]
	for directory in paths[1:]:
		if stack[-1].endswith('.jpeg') or stack[-1].endswith('.gif'):
			totallgth += sum([len(d) - leadingSpace(d) + 1 for d in stack[:-1]])
		while len(stack) and leadingSpace(stack[-1]) >= leadingSpace(directory):
			del stack[-1]
		stack.append(directory)
	if stack[-1].endswith('.jpeg') or stack[-1].endswith('.gif'):
			totallgth += sum([len(d) + 1 for d in stack[:-1]])
	return totallgth

def leadingSpace(s):
	cnt = 0
	for c in s:
		if c != ' ':
			break
		cnt += 1
	return cnt

def main():
	x = 1000000000
	print(solution1(x))
	print(solution2(41))
	print(solution3(623315))
	paths = 'dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif'
	print(pathSearch(paths))

if __name__ == '__main__':
	main()
