class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()
        for ind in range(len(nums)):
            if nums[ind]  in book:
                return True
            book.add(nums[ind])
        return False
