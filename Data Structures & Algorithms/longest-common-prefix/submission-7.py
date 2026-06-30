class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = []

        for loop in range(len(strs)):
            ans.append(len(strs[loop]))

        n = min(ans)
        
        ans = ''
        for loop in range(n):
            c = strs[0][loop]
            for i in range(1,len(strs)):
                if strs[i][loop] != c :
                    return ans
            ans = ans + c
        return ans

