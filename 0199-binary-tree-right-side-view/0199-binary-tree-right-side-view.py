# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rList = []
        def getRight(root, rList, level):
            if not root:
                return rList
            if level==len(rList):
                rList.append(root.val)
            
            getRight(root.right, rList, level+1)
            getRight(root.left, rList, level+1)

        getRight(root, rList, 0)
        
        return rList
        