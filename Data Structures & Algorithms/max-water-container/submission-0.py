class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights) -1 
        maxi = 0 

        while left < right : 
            if heights[left] > heights[right]: 
                cur = (right - left ) * heights[right]
            else:
                cur = (right - left) * heights[left]
            
            if cur > maxi: 
                maxi = cur 

            if heights[left] < heights[right]: 
                left = left + 1
            else:
                right = right -1 

        return maxi

            

        