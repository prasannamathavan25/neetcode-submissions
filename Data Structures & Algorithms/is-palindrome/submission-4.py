class Solution:
    def isPalindrome(self, s: str) -> bool:

        lp = 0 
        rp = len(s)-1

        while lp < rp :
            while not s[lp].isalnum() and lp < rp :
                lp = lp + 1
            while not s[rp].isalnum() and lp < rp :
                rp = rp - 1
            
            if s[lp].casefold() != s[rp].casefold():
                return False
            lp = lp + 1
            rp = rp - 1
        return True
            

        
            

               
        