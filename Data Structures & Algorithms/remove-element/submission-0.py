class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for loop in range(len(nums)):
            if val == nums[loop]: 
                count = count + 1
                nums[loop] = float('inf')
        
        nums.sort()
        return len(nums) - count
            


        