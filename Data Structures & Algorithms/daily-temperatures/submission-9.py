class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]

        stack = []

        for i, temperature in enumerate(temperatures):
            if not stack:
                stack.append((i, temperature))
            else:
                while stack and temperature > stack[-1][1]:
                    popped = stack.pop()
                    res[popped[0]] = i-popped[0]
                
                stack.append((i, temperature))

        return res