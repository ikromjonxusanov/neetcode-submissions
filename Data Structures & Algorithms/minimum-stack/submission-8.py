class MinStack:

    def __init__(self):
        self.stack = []

        self.min_stack = []
        self.min_val = None

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
            self.min_val = value
        elif self.min_val > value:
            self.min_stack.append(value)
            self.min_val = value
        else:
            self.min_stack.append(self.min_val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min_val = self.min_stack[-1] if self.min_stack else None
        
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
        
    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()