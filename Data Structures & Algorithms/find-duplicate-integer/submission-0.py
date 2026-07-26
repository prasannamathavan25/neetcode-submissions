class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for item in nums:
            if item in myset:
                return item
            myset.add(item)
            
        