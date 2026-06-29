class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book1 = dict()
        book2 = dict()
        
        if len(s) != len(t):
            return False
            
        for ind in range(len(s)):
            book1[s[ind]] = book1.get(s[ind], 0) + 1
            book2[t[ind]] = book2.get(t[ind], 0) + 1
            
        return book1 == book2
