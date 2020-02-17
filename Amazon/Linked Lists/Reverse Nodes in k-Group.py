"""
URL : https://leetcode.com/explore/interview/card/amazon/77/linked-list/2977/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_list(self, head):
        node1 = head
        node2 = head.next

        head.next = None
        while node1 is not None and node2 is not None:
            temp = node2.next
            node2.next = node1
            node1 = node2
            node2 = temp

        return node1, head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        count = 0
        current_node = head
        sub_list_head, new_head, prev_sub_last_node = None, None, None
        is_first = False

        while current_node:
            count += 1
            if count == 1:
                sub_list_head = current_node

            if count == k:
                temp = current_node.next
                current_node.next = None
                first_node, last_node = self.reverse_list(sub_list_head)
                if prev_sub_last_node:
                    prev_sub_last_node.next = first_node
                prev_sub_last_node = last_node
                last_node.next = temp
                current_node = temp
                count = 0
                if not is_first:
                    is_first = True
                    new_head = first_node
            else:
                current_node = current_node.next

        return new_head if new_head else head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

head = Solution().reverseKGroup(n1, 1)
print(head)