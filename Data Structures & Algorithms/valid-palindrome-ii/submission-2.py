class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1 


        


        def check(lp , rp):
            while lp < rp:
                if s[lp] != s[rp]:
                    return False
                lp = lp + 1
                rp = rp -1
            return True
        
        while left < right : 
            if s[left] != s[right]:
                return check(left + 1 , right) or check(left , right -1)
            left = left + 1
            right = right -1 
        return True
        
            
