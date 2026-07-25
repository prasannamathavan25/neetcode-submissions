class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i,c in enumerate(s):
            if c != ']':
                stack.append(c)
            else:
                string =''
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()

                n=''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                n = int(n)

                stack.append(n*string)
        
        return ''.join(stack)
        


        