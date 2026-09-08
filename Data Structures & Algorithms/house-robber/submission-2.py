class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr=[0]*n
        arr[n-1]= nums[n-1]
        arr[n-2]= max(nums[n-1],nums[n-2])
        for j in range(n - 3, -1, -1):
            arr[j] = max(nums[j] + arr[j + 2], arr[j + 1])
        return arr[0]

    
    
    

        