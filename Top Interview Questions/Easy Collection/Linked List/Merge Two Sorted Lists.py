"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergedList = None
        currentNodeMergedList = None
        currentNodeL1 = l1
        currentNodeL2 = l2

        while currentNodeL1 and currentNodeL2:
            if currentNodeL1.val < currentNodeL2.val:
                if currentNodeMergedList is None:
                    currentNodeMergedList = ListNode(currentNodeL1.val)
                    mergedList = currentNodeMergedList
                else:
                    currentNodeMergedList.next = ListNode(currentNodeL1.val)
                    currentNodeMergedList = currentNodeMergedList.next

                currentNodeL1 = currentNodeL1.next
            else:
                if currentNodeMergedList is None:
                    currentNodeMergedList = ListNode(currentNodeL2.val)
                    mergedList = currentNodeMergedList
                else:
                    currentNodeMergedList.next = ListNode(currentNodeL2.val)
                    currentNodeMergedList = currentNodeMergedList.next

                currentNodeL2 = currentNodeL2.next

        if currentNodeL1 is not None:
            while currentNodeL1:
                if currentNodeMergedList is None:
                    currentNodeMergedList = ListNode(currentNodeL1.val)
                    mergedList = currentNodeMergedList
                else:
                    currentNodeMergedList.next = ListNode(currentNodeL1.val)
                    currentNodeMergedList = currentNodeMergedList.next
                currentNodeL1 = currentNodeL1.next

        if currentNodeL2 is not None:
            while currentNodeL2:
                if currentNodeMergedList is None:
                    currentNodeMergedList = ListNode(currentNodeL2.val)
                    mergedList = currentNodeMergedList
                else:
                    currentNodeMergedList.next = ListNode(currentNodeL2.val)
                    currentNodeMergedList = currentNodeMergedList.next
                currentNodeL2 = currentNodeL2.next
        return mergedList