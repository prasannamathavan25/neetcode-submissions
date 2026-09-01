class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]

        for item in operations:
            if item == '+':
                new = stack[-1] + stack[-2]
                stack.append(new)
            elif item == "D":
                new = stack[-1]*2
                stack.append(new)
            elif item == "C":
                stack.pop()
            else:
                stack.append(int(item))
        
        return sum(stack)
     
        


            
            
        