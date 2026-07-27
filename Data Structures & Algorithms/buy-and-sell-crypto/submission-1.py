class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0,1
        max_ans = 0 

        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                max_ans = max(max_ans , profit)
            else:
                l = r 
            r = r + 1 
        return max_ans