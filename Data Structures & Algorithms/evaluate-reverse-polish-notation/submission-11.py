class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+*/-":
                o_1, o_2 = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(o_2 + o_1)
                elif t == "-":
                    stack.append(o_2 - o_1)
                elif t== "*":
                    stack.append(o_2 * o_1)
                else:
                    stack.append(math.trunc(o_2 / o_1))

            else:
                stack.append(int(t))

            print(stack, t)

        return stack.pop()
    
