class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        while(n>=1):
            nums1[pos] = nums2[n-1]
            pos = pos -1
            n = n - 1
            
        nums1.sort()    
            
        