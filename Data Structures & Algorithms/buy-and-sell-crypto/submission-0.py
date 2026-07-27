class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        max_ans = 0 
        n = len(prices)

        for l in range(n-1):
            for r in range(l+1,n):
                val = prices[r] - prices[l]
                if val > max_ans:
                    max_ans = val
        
        return max_ans