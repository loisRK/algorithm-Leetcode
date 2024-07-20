# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []

        def getLeaf(root, leaf):
            if not root:
                return False
            
            if root.left:
                getLeaf(root.left, leaf)
            if root.right:
                getLeaf(root.right, leaf)
            if not root.right and not root.left:
                leaf.append(root.val)
        
        getLeaf(root1, leaf1)
        getLeaf(root2, leaf2)

        if leaf1 == leaf2:
            return True
        else:
            return False
