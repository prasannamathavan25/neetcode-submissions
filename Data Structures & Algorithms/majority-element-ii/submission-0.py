class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        book = dict()
        ans = []

        for loop in range(len(nums)): 
            book[nums[loop]] = 1 + book.get(nums[loop] , 0 )
           
        for key in book.keys():
            if book[key] > len(nums) // 3 : 
                ans.append(key)
        
        return ans

        
        