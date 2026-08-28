class Solution:

    def merge(self, nums1, m, nums2, n):
        for loop  in range(n):
            nums1[m+loop] = nums2[loop]
        print(nums1.sort())

       