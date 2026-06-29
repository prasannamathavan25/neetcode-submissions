class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()
        for ind in range(len(nums)):
            val = nums[ind]
            if val  in book:
                return True
            book.add(val)
        return False
