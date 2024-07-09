class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer=[]
        ns=[]
        ms=[]
        if len(nums1) <= len(nums2):
            ns = nums1
            ms = nums2

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    answer.append(nums1[i])
                    del nums2[j]

                    break

        
        return answer
        