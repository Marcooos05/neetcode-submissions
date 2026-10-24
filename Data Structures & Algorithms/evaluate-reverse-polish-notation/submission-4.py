class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Done a similar question before, key idea here that I plan to implement is iterate through the input stack, push numbers, if an operator is met, pop the top 2 values, then proceed with the operation, once done push the calculated value back into the stack.
        #Stupid Fact: -0.04545... rounds down to -1 (away from zero / toward negative infinity)
        stack = []
        for op in tokens:
            if op in ["+", "-", "*", "/"]:
                j = stack.pop()
                i = stack.pop()
                if op == "+":
                    val = i+j
                elif op == "-":
                    val = i-j
                elif op == "*":
                    val = i*j
                else:
                    val = i//j if i*j > 0 else -(-i//j)
                stack.append(val)
            else:
                stack.append(int(op))
        return stack[0]