class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        ## Interesting algorithm from the Neetcode explanation, to have another stack to hold the min Value given the new val was added to the list, so the minStack will store the min val of the new stack at the top of the list. Hence the min Value and the added value will share the same index. At which when the val is popped we need to also pop from the minStack.
        ## Storing a single min value will run into issues if the val added is a duplicate, which I initially tried and then subsequently gave up, bcos making that O(1) time made the push and pop way more complex as it was difficult to manage duplicated values in O(1) time.
        if self.minStack:
            minVal = min(val, self.minStack[-1])
            self.minStack.append(minVal)
        else:
            self.minStack.append(val)
            
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
