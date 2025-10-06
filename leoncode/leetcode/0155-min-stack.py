# 155 - https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack, self.minStack = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
            return
        if val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None