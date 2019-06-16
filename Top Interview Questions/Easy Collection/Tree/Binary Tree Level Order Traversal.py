"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        result = []

        def helper(l):
            valueList = []
            nextNodeList = []

            for node in l:
                valueList.append(node.val)
                if node.left is not None:
                    nextNodeList.append(node.left)
                if node.right is not None:
                    nextNodeList.append(node.right)

            return valueList, nextNodeList

        if root is not None:
            l = [root]
            valueList, nextNodeList = helper(l)
            result.append(valueList)

            while len(nextNodeList) != 0:
                valueList, nextNodeList = helper(nextNodeList)
                result.append(valueList)

        return result


