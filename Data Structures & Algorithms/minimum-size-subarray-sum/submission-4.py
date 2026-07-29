class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , total = 0,0 
        ans = float('inf')

        for r in range(len(nums)):
            total = total + nums[r]
            while total >= target :
                ans = min(ans , r-l+1)
                total = total - nums[l]
                l = l + 1 
        return 0 if ans == float('inf') else ans

