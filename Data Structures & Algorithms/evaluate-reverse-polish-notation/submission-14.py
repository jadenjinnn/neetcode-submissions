class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-/*":
                o1 = int(stack.pop())
                o2 = int(stack.pop())


                if token =="+":
                    stack.append(o2+o1)
                elif token =="-":
                    stack.append(o2-o1)
                elif token =="*":
                    stack.append(o2*o1)
                elif token =="/":
                    stack.append(math.trunc(o2/o1))

            else:
                stack.append(token)

        return int(stack[-1])