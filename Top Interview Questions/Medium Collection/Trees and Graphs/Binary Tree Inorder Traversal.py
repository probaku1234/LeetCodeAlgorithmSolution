class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "val : {}".format(self.val)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        stack = []
        output = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                output.append(current.val)
                current = current.right
            else:
                break

        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print s.inorderTraversal(root)
