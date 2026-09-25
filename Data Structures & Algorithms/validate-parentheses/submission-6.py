class Solution:
    #Runtime 27ms|Beats 94.70%
    #Memory 7.9 MB|Beats 22.75%
    #Review
    #1. First question reviewing the stack data structure, honestly FILO concept isn't too difficult to understand. But dang did I fall into all the common pitfalls like indexing the stack when it is empty, so failing to check the stack. And not checking if the stack is empty at the end. 
    #2. The algorithm itself was definitely familiar so that was useful. Would love to see how stack is useful for other use cases in the future. 
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
    def isValid_firstAttempt(self, s: str) -> bool:
        array = []
        for char in s:
            if char in {'{', '[', '('}:
                array.append(char)
            elif len(array) > 0:
                if char == ')' and array[-1] != '(':
                    return False
                elif char == ']' and array[-1] != '[':
                    return False 
                elif char == '}' and array[-1] != '{':
                    return False
                else:
                    array.pop()
                    continue
            else:
                return False
        return array == []