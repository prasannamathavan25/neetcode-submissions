class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0 

        for i in range(1, len(prices)): 
            gain = prices[i] - prices[i-1]
            print(gain)
            if gain > 0 : 
                ans = ans + gain 
                print(ans)
        
        return ans
        