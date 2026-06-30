class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        nums.sort()
        ind = (len(nums)-1) // 2 
        print(ind)
        return nums[ind]