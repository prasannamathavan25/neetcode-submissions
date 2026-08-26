class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()
        for item in nums:
            if item in book:
                return True
            book.add(item)
        return False