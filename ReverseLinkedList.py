__author__ = 'Dimitri Zhang'
from ListNode import ListNode
from ListNode import createList
from ListNode import printList
cnt = 0
def myreverse(pre, current):
	if not current:
		return pre
	t = current.next
	current.next = pre
	return myreverse(current, t)

def increment():
	# global cnt
	# cnt += 1
	print(cnt)

def fun():
	a = 1
	def subfun():
		print(a)
	subfun()

def main():
	l1 = createList([1,2,3])
	# global cnt
	cnt = 0
	increment()
	print(cnt)
	# fun()
	# reversedl1 = myreverse(None, l1)
	# printList(reversedl1)

if __name__ == '__main__':
	main()