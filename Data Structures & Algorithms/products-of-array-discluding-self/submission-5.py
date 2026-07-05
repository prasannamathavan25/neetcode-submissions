class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [1]*n 

        for loop in range(1,n):
            ans[loop] = ans[loop-1] * nums[loop-1]
        
        print(ans)
        
        suf = nums[-1]
        for loop in range(n-2 ,-1,-1):
            ans[loop] = ans[loop]*suf 
            suf = suf * nums[loop]
        print(ans)

        return ans


        