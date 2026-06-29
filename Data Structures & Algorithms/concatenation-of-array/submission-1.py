class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        for loop in range(len(nums)):
            nums.append(nums[loop])

        return nums
        