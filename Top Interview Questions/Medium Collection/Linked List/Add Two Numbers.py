"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def helper(self, head):
        length = 0
        output = 0
        current_node = head

        while current_node:
            output += current_node.val * pow(10, length)
            current_node = current_node.next
            length += 1

        return output

    def addTwoNumbers(self, l1, l2):
        num1 = self.helper(l1)
        num2 = self.helper(l2)
        sum = num1 + num2
        length = len(str(sum))
        output = None
        current_node = None

        for i in range(int(length)):
            temp = ListNode(sum % 10)
            if output:
                current_node.next = temp
                current_node = temp
            else:
                output = temp
                current_node = temp
            sum /= 10

        return output

l1 = ListNode(8)
l2 = ListNode(9)
l3 = ListNode(9)
l4 = ListNode(2)

l1.next = l2
l2.next = l3

s = Solution()
print s.addTwoNumbers(l1,l4)