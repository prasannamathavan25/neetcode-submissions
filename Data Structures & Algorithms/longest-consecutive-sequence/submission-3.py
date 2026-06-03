class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        left = 0 
        right = 1 
        maxi = 1
        count = 0

        if len(nums) == 0 :
            return 0

        while right < len(nums): 
            if nums[right] == nums[right-1] + 1 : 
                if right - left + 1 > maxi : 
                    maxi = right -left + 1
                right = right + 1 
            else:
                left = right 
                right = left + 1 

        
        return maxi