from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        book = Counter(nums)
        ans = []
        for item in book:
            if book[item] > len(nums) //3 :
                ans.append(item)
           
        return ans


       
        
        