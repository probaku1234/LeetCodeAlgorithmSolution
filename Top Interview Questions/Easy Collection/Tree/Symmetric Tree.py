"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.help(root, root)
