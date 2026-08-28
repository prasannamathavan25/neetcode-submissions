class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()

        ans = 1 
         
        for num in nums : 
            if num >0 and ans == num : 
                ans = ans + 1 
            
        return ans
            

        