"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/342/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
g = ListNode(2)
h = ListNode(6)
g.next = h
Solution().mergeKLists([a, d, g, ListNode(7)])

current = a
while current:
    print(current.val, end=" ")
    current = current.next