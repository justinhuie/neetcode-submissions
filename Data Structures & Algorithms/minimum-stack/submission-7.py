class MinStack:

    # Initalize class with two stacks
    # one to track the min value of stack  and another to track the curr stack
    def __init__(self):
        self.stack = []
        self.minStack = []

    # We can push the element on the cur stack
    # for the minStack we check if the value is less than the current minStack
    # if no minstack we just push
    # [3, 4, 7, 1]
    # [3, 1]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
    
    # Can just pop from stack
    # Set the pop value to val
    # if val == top of minStack then pop from minStack

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
  
    def top(self) -> int:
        return self.stack[-1]
      
    def getMin(self) -> int:
        return self.minStack[-1]

      
