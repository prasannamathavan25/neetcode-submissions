from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        book1 = [0]*26
        book2 = [0]*26

        for loop in range(len(s)):
            c1 = s[loop]
            c2 = t[loop]
            i1 = ord('a') - ord(c1)
            i2 = ord('a') - ord(c2)

            book1[i1] = book1[i1] + 1
            book2[i2] = book2[i2] + 1
        
        return book1 == book2
        
        


        

        