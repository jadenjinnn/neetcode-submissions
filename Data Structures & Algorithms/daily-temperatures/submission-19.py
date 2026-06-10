class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append((i, temperatures[i]))

        return result