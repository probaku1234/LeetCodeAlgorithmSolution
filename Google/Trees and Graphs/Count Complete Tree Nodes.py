"""
URL : https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3071/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def depth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d

    def exists(self, idx, d, node):
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1

        return node is not None

    def countNodes2(self, root):
        if not root:
            return 0

        d = self.depth(root)
        if d == 0:
            return 1

        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return (2 ** d - 1) + left


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(Solution().countNodes(root))