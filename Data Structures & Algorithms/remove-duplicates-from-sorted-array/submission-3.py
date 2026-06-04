class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur = nums[0]
        p1 = 1
        p2 = 1 
        count = 0

        while p2 < len(nums):
            if nums[p2] > nums[p1-1] : 
                nums[p1] = nums[p2]
                p1 = p1 + 1 
                p2 = p2 + 1 
            else:
                p2 = p2 + 1
                count = count +  1

        for loop in range(count):
            nums.pop()
        
        
        return len(nums)
        
        

        