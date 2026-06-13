class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        pair = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack.pop() != pair[c]:
                    return False

        return not len(stack)>0 