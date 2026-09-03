class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for loop in range(n):
            if nums[loop] == target:
                return loop
        return -1
    
