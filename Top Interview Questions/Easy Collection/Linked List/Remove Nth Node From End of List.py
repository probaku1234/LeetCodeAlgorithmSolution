"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            head = head.next
            return head

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head