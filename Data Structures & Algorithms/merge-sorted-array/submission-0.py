class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for loop in range(n):
            nums1.pop()
        
        for loop in range(len(nums2)):
            nums1.append(nums2[loop])
        
        nums1.sort()
        
    



        