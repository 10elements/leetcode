__author__ = 'Dimitri Zhang'

class ListNode(object):
    """docstring for LstNode"""

    def __init__(self, x):
        """
        initialization
        """
        self.val = x
        self.next = None

def createList(nums):
    """
    """
    l = len(nums)
    if not l:
        return None
    r = ListNode(0)
    result = r
    for i in range(l):
        r.val = nums[i]
        if i == l - 1:
            r.next = None
            break
        r.next = ListNode(0)
        r = r.next
    return result

def printList(node):
    nums = []
    while node != None:
        nums.append(node.val)
        node = node.next
    print(nums)

def main():
	l1 = createList([1,2,3])
	printList(l1)

if __name__ == '__main__':
	main()