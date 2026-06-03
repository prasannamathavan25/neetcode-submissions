class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]*len(nums)

        for loop in range(1,len(nums)):
            pre[loop] = pre[loop-1]* nums[loop-1]
        
        
        suf = 1 

        for loop in range(len(nums)-1 ,-1 , -1):
            pre[loop] = suf * pre[loop]
            suf = suf*nums[loop]

        return pre
        
       

        
       


       