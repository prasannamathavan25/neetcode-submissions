class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        # Helper function for a standard linear line of houses
        def rob_linear(houses: List[int]) -> int:
            prev2 = 0 # Represents dp[i-2]
            prev1 = 0 # Represents dp[i-1]
            
            for amount in houses:
                # Max of (rob current house + skip previous) OR (skip current house)
                current = max(prev2 + amount, prev1)
                prev2 = prev1
                prev1 = current
                
            return prev1

        # Max of skipping the last house vs skipping the first house
        ans1 = rob_linear(nums[:-1])
        ans2 = rob_linear(nums[1:])
        
        return max(ans1, ans2)
