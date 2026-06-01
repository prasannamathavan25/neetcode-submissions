class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        book = dict()

        for num in nums:
            book[num] = 1 + book.get(num, 0)

        arr = sorted(book, key=book.get, reverse=True)

        return arr[:k]