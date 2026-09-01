class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        book = '+*-/'

        for item in tokens:
            if item not in book:
                stack.append(int(item))
                continue
            if item == '+':
                new = stack.pop() + stack.pop()
                stack.append(new)
            elif item == "*":
                new = stack.pop() * stack.pop()
                stack.append(new)
            elif item == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
        
        return stack[-1]