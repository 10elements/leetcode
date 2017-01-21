def solution(root):
	res = []
	inOrder(root, res)
	i = 0
	stack = [root]
	visited = {}
	while len(stack):
		top = stack[-1]
		if not top.left and not top.right:
			visited[top] = True
			stack.pop()
			top.val = sum(res[i:])
			i += 1
		elif not top.left or top.left in visited:
			visited[top] = True
			stack.pop()
			top.val = sum(res[i:])
			i += 1
			if top.right:
				stack.append(top.right)
		elif top.left:
			stack.append(top.left)
	return root
	
def inOrder(root, res):
	if root:
		self.inOrder(root.left, res)
		res.append(root.val)
		self.inOrder(root.right, res)