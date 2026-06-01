class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = set()
        for loop in range(len(nums)):
            if nums[loop] in book: 
                return True
            book.add(nums[loop])
        return False
        