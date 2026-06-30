class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
       
        n = len(strs[0])
        for loop in range(len(strs)):
            cur = len(strs[loop])
            if cur < n : 
                n = cur

        for loop1 in range(n):
            cur = strs[0][loop1]
            for loop2 in range(1,len(strs)):
                if cur != strs[loop2][loop1]:
                    return ans
            ans = ans + cur

        return ans


        