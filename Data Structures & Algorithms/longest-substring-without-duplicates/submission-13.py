class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxl = 0 
        lp = 0 

        for rp in range(len(s)):
            while s[rp] in window :
                window.remove(s[lp])
                lp = lp + 1
            window.add(s[rp])
            maxl = max(maxl , rp - lp + 1)
        return maxl
