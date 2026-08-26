from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book = defaultdict(int)

        for item in nums:
            book[item] = book[item] + 1
            if book[item] > len(nums) // 2:
                return item
            
            

            