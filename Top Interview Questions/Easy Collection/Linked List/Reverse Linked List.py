"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentNode = head
        reversedNode = None

        while currentNode is not None:
            tempNode = ListNode(currentNode.val)

            if reversedNode is None:
                reversedNode = tempNode
            else:
                tempNode.next = reversedNode
                reversedNode = tempNode

            previouseNode = currentNode
            currentNode = currentNode.next

        return reversedNode