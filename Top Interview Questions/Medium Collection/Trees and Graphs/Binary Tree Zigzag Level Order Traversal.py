"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        direction = 0

        def helper(l, d):
            valueList = []
            nextNodeList = []

            for node in l:
                valueList.append(node.val)
                if node.left is not None:
                    nextNodeList.append(node.left)
                if node.right is not None:
                    nextNodeList.append(node.right)

            if d == 1:
                valueList.reverse()

            return valueList, nextNodeList

        if root is not None:
            l = [root]
            valueList, nextNodeList = helper(l, direction)
            direction ^= 1
            result.append(valueList)

            while len(nextNodeList) != 0:
                valueList, nextNodeList = helper(nextNodeList, direction)
                direction ^= 1
                result.append(valueList)

        return result

root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
n5 = TreeNode(21)
n6 = TreeNode(7)

root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
n1.left = n5
n1.right = n6

s = Solution()
print(s.zigzagLevelOrder(root))