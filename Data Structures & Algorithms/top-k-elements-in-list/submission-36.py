from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = dict()
        for item in nums:
            if item not in book:
                book[item] = 0 
            book[item] += 1 
        sorted_book = sorted(book.items() , key = lambda item:item[1] , reverse = True)
        
        ans = []
        for loop in range(k):
            ans.append(sorted_book[loop][0])
        
        return ans


        
