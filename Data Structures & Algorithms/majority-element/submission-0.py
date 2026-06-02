class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        book = dict()

        for loop in range(len(nums)):
            book[nums[loop]] = 1 + book.get(nums[loop] , 0 )
            if book[nums[loop]] > len(nums) // 2 : 
                return nums[loop]
        
        return max(book , key = book.get)
        