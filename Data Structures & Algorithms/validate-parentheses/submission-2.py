class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {
            "(":")",
            "{":"}",
            "[":"]",
        }

        for char in s:
            print(stack)
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                elif not match[stack.pop()] == char:
                    return False 

        if not stack:
            return True
        else:
            return False