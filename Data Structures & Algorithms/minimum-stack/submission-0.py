import math
class MinStack:

    def __init__(self):
        self.minimum = math.inf
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append((val, self.minimum))
        if val < self.minimum:
            self.minimum = val
        

    def pop(self) -> None:
        _, prevmin = self.stack.pop()
        self.minimum = prevmin
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.minimum
        
