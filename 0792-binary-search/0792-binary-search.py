class Solution(object):
    def search(self, nums, target):

        def binarySearch(left, right):
            if left <= right:
                mid = (left + right)//2

                if target > nums[mid]:
                    return binarySearch(mid+1, right)
                elif target < nums[mid]:
                    return binarySearch(left, mid-1)
                else:
                    return mid
            else:
                return -1
        
        return binarySearch(0,len(nums)-1)