class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*n
        if( n==1): return nums[0]
        arr[0] = nums[0]

        arr[1] = max(nums[0], nums[1])
        for j in range(2,n):
            arr[j] = max(arr[j-1] , arr[j-2] + nums[j])
        return arr[-1]


        
    
    
    

        