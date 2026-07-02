class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        n = 3 
        count = [0] * n 
        
        for ptr in range(len(nums)):
            val = nums[ptr]
            count[val] += 1 
        print(count)
        p1 = 0 
        p2 = 0
        while p1 < n:
            t = count[p1]
            for _ in range(t):
                print('1')
                nums[p2] = p1
                p2 = p2 + 1
            p1 = p1+1
        return nums
                
        