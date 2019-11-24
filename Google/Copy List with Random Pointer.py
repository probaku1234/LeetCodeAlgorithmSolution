"""
URL : https://leetcode.com/explore/interview/card/google/60/linked-list-5/3066/
"""


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        copy_node = {}

        current_node = head
        while current_node:
            copy_node[current_node] = Node(current_node.val, None, None)
            current_node = current_node.next

        current_node = head
        while current_node:
            if current_node.next:
                copy_node[current_node].next = copy_node[current_node.next]
            if current_node.random:
                copy_node[current_node].random = copy_node[current_node.random]
            current_node = current_node.next

        return copy_node[head]

head = Node(1, None, None)
node1 = Node(2, None, None)
head.next = node1
head.random = head
Solution().copyRandomList(head)