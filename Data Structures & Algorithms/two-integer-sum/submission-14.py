class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = dict()

        for loop in range(len(nums)):
            num = nums[loop]
            diff = target - num
            if diff in book:
                return [book[diff] , loop]
            book[num] = loop
        
        