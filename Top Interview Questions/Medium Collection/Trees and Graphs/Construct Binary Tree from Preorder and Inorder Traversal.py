"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])  # The first node of preorder list is the root node of this tree
        # Nodes before root node in inorder list are left sub tree
        # Nodes after root node in inorder list are right sub tree
        index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])

        return root


