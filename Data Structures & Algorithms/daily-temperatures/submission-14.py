class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()

                sol[index] = i-index

            stack.append((i, temperatures[i]))

            print(stack, sol)

        return sol