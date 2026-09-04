class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0
        lp = 0 

        for rp in range(len(s)):
            # If the character is already in our window,
            # shrink the window from the left until the duplicate is removed
            while s[rp] in window:
                window.remove(s[lp])
                lp += 1
            
            # Add the current character to the window
            window.add(s[rp])
            
            # Track the maximum length seen so far
            ans = max(ans, rp - lp + 1)
            
        return ans
