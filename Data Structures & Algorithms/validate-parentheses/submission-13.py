class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        book = {
            ')' : "(",
            ']' : '[',
            '}' : '{'   }
        
        for item in s : 
            if item not in book:
                stack.append(item)
                continue
            if len(stack) == 0 :
                return False
            if stack[-1] == book[item]:
                stack.pop()
                continue
            return False
        return len(stack) == 0 