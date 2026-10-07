class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # Table to store the minimum cost to reach each step
        dp = [0] * (n + 1)
        
        # Start looping from step 2 up to the top (n)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return dp[n]
