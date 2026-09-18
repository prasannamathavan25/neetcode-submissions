class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()

        ind = len(nums)
        for loop in range(len(nums)):
            if nums[loop] == val:
                ind = loop
                break

        loop = ind
        while loop < len(nums) and nums[loop] == val:
            nums.pop(loop)

        return len(nums)