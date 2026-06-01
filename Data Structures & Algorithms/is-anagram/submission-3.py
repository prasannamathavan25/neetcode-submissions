class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book1 = dict()
        book2 = dict()

        for loop in range(len(s)):
            book1[s[loop]] = 1 + book1.get(s[loop], 0)
        for loop in range(len(t)):
            book2[t[loop]] = 1 + book2.get(t[loop], 0)

        return book1 == book2
        