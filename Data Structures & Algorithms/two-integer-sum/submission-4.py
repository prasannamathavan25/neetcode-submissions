class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = dict()

        for ind in range(len(nums)): 
            rem = target - nums[ind]
            if rem in book : 
                return [book[rem] , ind ]
            
            book[nums[ind]] = ind 
