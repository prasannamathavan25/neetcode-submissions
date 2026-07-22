class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations : 
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                continue
            if op == 'D':
                stack.append(stack[-1] * 2)
                continue 
            if op == 'C':
                stack.pop()
                continue
            stack.append(int(op))
        
        ans = 0 
        for num in stack:
            ans = ans + num 
        
        return ans
        

        


            
            
        