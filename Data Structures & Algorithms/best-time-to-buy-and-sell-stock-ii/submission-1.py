class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        n = len(prices)

        for loop in range(n-1):
            if prices[loop+1] - prices[loop] > 0 :
                ans = ans + prices[loop+1] - prices[loop]
        return ans
            


       