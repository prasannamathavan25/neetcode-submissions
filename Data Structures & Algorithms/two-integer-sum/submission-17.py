class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = dict()

        for loop in range(len(nums)):
            rem = target - nums[loop]
            print(rem)
            if rem in book : 
                print(rem)
                return [book[rem] , loop]
            else:
                book[nums[loop]] = loop 
        