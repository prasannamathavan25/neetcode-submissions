class Solution:

    def encode(self, strs: List[str]) -> str:

        code = ''
        for loop in range(len(strs)):
            leng = len(strs[loop])
            code = code + '#' + str(leng) + '#' + strs[loop]
        code = code + "#"
        return code


    def decode(self, s: str) -> List[str]:

        ans = []
        i = 0
        while i < len(s)-1:
            if s[i] == '#':
                i += 1
                num = s[i]
                while s[i+1] != '#':
                    num = num + s[i+1]
                    i += 1
                num = int(num)
                i += 2
                cur = s[i:i+num]
                ans.append(cur)
                i = i + num

        return ans