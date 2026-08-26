class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''

        for loop in range(len(strs[0])):
            for s in strs:
                if loop == len(s) or s[loop] != strs[0][loop] :
                    return ans
            ans += strs[0][loop]
        return ans




        
        