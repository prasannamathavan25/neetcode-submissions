class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set(nums)
        return len(book) != len(nums)