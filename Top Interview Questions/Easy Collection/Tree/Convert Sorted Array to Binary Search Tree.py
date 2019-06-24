"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def BSTinsertBalanced(root, nums):
            if nums == []:
                return None
            else:
                root = TreeNode(nums[len(nums) // 2])
                root.left = BSTinsertBalanced(root.left, nums[:len(nums) // 2])
                root.right = BSTinsertBalanced(root.right, nums[len(nums) // 2 + 1:])
                return root

        newRoot = TreeNode(0)
        return BSTinsertBalanced(newRoot, nums)