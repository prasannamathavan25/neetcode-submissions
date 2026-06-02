class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        book = dict()
        max_count = 0 
        ind = 0 

        for loop in range(len(nums)):
            book[nums[loop]] = 1 + book.get(nums[loop] , 0 )
            if book[nums[loop]] > len(nums) // 2 : 
                return nums[loop]
            
            if book[nums[loop]] > max_count : 
                max_count = book[nums[loop]]
                ind = loop

        return nums[ind]
        
        
        