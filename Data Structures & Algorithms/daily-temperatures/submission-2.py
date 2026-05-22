class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t = stack.pop()
                res[t[1]] = i-t[1]

            stack.append((temperatures[i],i))

            print(stack, res)

        return res

