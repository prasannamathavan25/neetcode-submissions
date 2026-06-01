class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book1 = Counter(s)
        book2 = Counter(t)

        return book1 == book2 
        