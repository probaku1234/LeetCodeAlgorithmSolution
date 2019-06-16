"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pos = -1
        index = 0
        currentNode = head

        while currentNode is not None:
            if currentNode.val == 't':
                pos = index
                break
            else:
                currentNode.val = 't'

            index += 1
            currentNode = currentNode.next

        if pos == -1:
            return False
        else:
            return True
