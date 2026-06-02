class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        
        
        nums.sort()
        ind = len(nums) // 2
        return nums[ind]