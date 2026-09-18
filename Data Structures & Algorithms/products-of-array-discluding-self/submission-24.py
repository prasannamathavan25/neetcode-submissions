class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for loop in range(1,len(nums)):
            prefix[loop] = prefix[loop-1] * nums[loop-1]
        
        mul = 1 

        for loop in range(len(nums)-1 , -1,-1):
            prefix[loop] = prefix[loop]*mul
            mul = mul * nums[loop]

        return prefix
       
    