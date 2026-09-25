class Solution:
    def isValid(self, s: str) -> bool:
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