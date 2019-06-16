"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        secondHead = slow.next
        slow.next = None

        p1 = secondHead
        p2 = p1.next

        while p1 is not None and p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp

        secondHead.next = None

        p = p1 if p2 is None else p1
        q = head

        while p is not None:
            if p.val != q.val:
                return False

            p = p.next
            q = q.next

        return True
