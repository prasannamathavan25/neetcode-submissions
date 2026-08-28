class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lp = 0 
        rp = len(s)-1

        while lp < rp : 
            s[lp] , s[rp] = s[rp] , s[lp]
            lp = lp + 1
            rp = rp - 1

        return s
            

        