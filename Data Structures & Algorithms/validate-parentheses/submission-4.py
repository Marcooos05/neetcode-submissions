class Solution:
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