class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for loop in range(1,n):
            prefix[loop] = prefix[loop-1] * nums[loop-1]
        for loop in range(n-2,-1,-1):
            suffix[loop] = suffix[loop+1] * nums[loop+1]
        
        ans = [prefix[i] * suffix[i] for i in range(n)]
        return ans