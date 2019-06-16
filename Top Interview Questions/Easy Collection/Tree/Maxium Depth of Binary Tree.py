"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1

