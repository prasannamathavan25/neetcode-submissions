class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0 
        left , right = 0 , len(height) -1 
        ans = 0 
        max_l = 0 
        max_r = 0 

        while left < right : 
            if height[left] <= height[right]: 
                cur = max_l - height[left]
                if cur > 0 : 
                    ans = ans + cur 
                if height[left] > max_l:
                    max_l = height[left]
                left = left + 1
            else:
                cur = max_r - height[right]
                if cur > 0 :
                    ans = ans + cur 
                if height[right] > max_r : 
                    max_r = height[right]
                right = right -1 
        
        return ans
            

    
        