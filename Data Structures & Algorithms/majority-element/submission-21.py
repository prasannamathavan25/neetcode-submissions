from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book = dict()
        for item in nums:
            if item not in book:
                book[item] = 1
            else:
                book[item] = book[item]  + 1
        
        new_book = sorted(book.items() , key = lambda p:p[1])
        return new_book[-1][0]

            