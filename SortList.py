from ListNode import ListNode, createList, printList
import sys
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        t = p1.next
        p1.next = None
        return self.merge(self.sortList(head), self.sortList(t))
        
    def merge(self, l1, l2):
        if (not l1) and l2:
            return l2
        if (not l2) and l1:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

def main():
    c = Solution()
    l = createList([1])
    printList(c.sortList(l))

if __name__ == '__main__':
    main()