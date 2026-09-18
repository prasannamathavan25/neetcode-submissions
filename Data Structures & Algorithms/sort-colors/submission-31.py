from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        book = defaultdict(int)
        for num in nums:
            if num not in book:
                book[num] = 0
            book[num] = book[num] + 1
        
        book = sorted(book.items(), key=lambda item: item[0])
        
        i = 0
        for item in book:
            for _ in range(item[1]):
                nums[i] = item[0]
                i = i + 1
