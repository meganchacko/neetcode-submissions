class Solution:
    def isValid(self, s: str) -> bool:
        new_s = s.replace(" ", "")
        stack = []

        if len(new_s) % 2 != 0:
            return False
        
        if new_s[0] == ')' or new_s[0] == ']' or new_s[0] == '}':
            return False

        for char in new_s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            if char == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False
            elif char == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False


        return not stack

        
