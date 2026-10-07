class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [None]*(n+1)

        def options(i):
            if i == 1: 
                return 1 
            if i == 2 :
                return 2 
            
            if arr[i] is not None:
                return arr[i]
            
            arr[i] = options(i-1) + options(i-2)
            return arr[i]
        
        return options(n)
        
    

            



        