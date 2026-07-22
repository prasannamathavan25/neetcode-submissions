class Solution:
    def isValid(self, s: str) -> bool:
        book = {")": '(', '}': "{", ']': '['}
        arr = []

        for item in s:
            if item in book.values():
                arr.append(item)
                continue
            
            if not arr or arr[-1] != book[item]:
                return False
                
            arr.pop()
            
        return len(arr) == 0
