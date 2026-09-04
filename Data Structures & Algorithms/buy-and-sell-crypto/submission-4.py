class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp,rp = 0 , 1 
        maxp = 0 

        while rp < len(prices):
            cur = prices[rp] - prices[lp]
            if cur > maxp :
                maxp = cur
            if cur > 0 :
                rp = rp + 1
            else:
                lp = rp
                rp = lp + 1
        
        return maxp


     


        