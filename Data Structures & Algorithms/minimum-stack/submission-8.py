class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        
        if len(self.s1) == 0 :
            self.s1.append(val)
            self.s2.append(val)
        else:
            self.s1.append(val)
            if val < self.s2[-1]:
                self.s2.append(val)
            else:
                self.s2.append(self.s2[-1])

    def pop(self) -> None:
        self.s2.pop()
        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]
        
