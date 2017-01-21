from ListNode import *
def rearrange(head):
	if head != None:
		pre = None
		p = head
		while p != None:
			if p.val >= 0:
				pre = p
				p = p.next
			else:
				pre.next = p.next
				p.next = head
				head = p
				p = pre.next
	return head

def main():
	head = createList([0, -1])
	head = rearrange(head)
	printList(head)

if __name__ == '__main__':
	main()