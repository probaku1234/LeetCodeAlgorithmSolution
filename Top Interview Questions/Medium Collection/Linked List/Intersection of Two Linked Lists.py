"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "val : {}".format(self.val)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        current_node_a, current_node_b = headA, headB
        length_a, length_b = 0, 0

        while current_node_a:
            length_a += 1
            current_node_a = current_node_a.next
        while current_node_b:
            length_b += 1
            current_node_b = current_node_b.next

        current_node_a, current_node_b = headA, headB
        for i in range(abs(length_b-length_a)):
            if length_a >= length_b:
                current_node_a = current_node_a.next
            else:
                current_node_b = current_node_b.next
        while current_node_b != current_node_a:
            current_node_a, current_node_b = current_node_a.next, current_node_b.next

        return current_node_a


l1 = ListNode("a1")
l2 = ListNode("a2")
l3 = ListNode("c1")
l4 = ListNode("c2")
l5 = ListNode("c3")
l6 = ListNode("b1")
l7 = ListNode("b2")
l8 = ListNode("b3")

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l6.next = l7
l7.next = l8
l8.next = l3

s = Solution()
print s.getIntersectionNode(l1, l6)