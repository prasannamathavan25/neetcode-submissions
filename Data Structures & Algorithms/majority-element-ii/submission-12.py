from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        book = dict(Counter(nums))
        print(book)
        ans = []
        for item in book:
            if book[item] > n //3 :
                ans.append(item)
           
        return ans


       
        
        