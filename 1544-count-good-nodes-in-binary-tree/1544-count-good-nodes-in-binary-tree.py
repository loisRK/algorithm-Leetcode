# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return 0

            total = 0
            if node.val >= maxVal:
                total = 1
                maxVal = node.val

            total += dfs(node.left, maxVal)
            total += dfs(node.right, maxVal)

            return total

        return dfs(root, root.val)