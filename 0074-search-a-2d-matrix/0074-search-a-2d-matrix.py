class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for arr in matrix:
            if target <= arr[-1]:
                if target in arr:
                    return True