class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        book1 = [0] * 26
        book2 = [0] * 26

        for ch in s1:
            book1[ord(ch) - ord('a')] += 1

        for i in range(len(s1)):
            book2[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:

            if book1 == book2:
                return True

            book2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1
            book2[ord(s2[r]) - ord('a')] += 1

        # Check the last window
        return book1 == book2