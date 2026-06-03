class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]*len(nums)

        for loop in range(1,len(nums)):
            pre[loop] = pre[loop-1]* nums[loop-1]
        
        suf = [1]*len(nums)
        for loop in range(len(nums)-2 , 0-1,-1):
            suf[loop] = suf[loop+1] * nums[loop+1]
        
        for loop in range(len(nums)):
            pre[loop] = pre[loop]*suf[loop]
        
        return pre

        
       


       