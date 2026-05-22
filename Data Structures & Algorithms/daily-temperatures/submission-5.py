class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0 for i in range(len(temperatures))]


        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))

            else:
                while stack and temp > stack[-1][1]:
                    popped = stack.pop()
                    sol[popped[0]] = i-popped[0]

                stack.append((i,temp))

            # print(stack, sol)

        return sol