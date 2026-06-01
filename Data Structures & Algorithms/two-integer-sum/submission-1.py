class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = dict()

        for loop in range(len(nums)):
            rem = target - nums[loop]

            if rem in book : 
              return [book[rem] , loop ]
            
            book[nums[loop]] = loop

        