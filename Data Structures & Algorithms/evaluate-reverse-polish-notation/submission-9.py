class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)

            try:
                stack.append(int(token))
            except ValueError:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(o2 - o1)
                elif token == "/":
                    o1 = stack.pop()
                    o2 = stack.pop()
                    stack.append(int(o2 / o1))
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
        
        return stack[-1]