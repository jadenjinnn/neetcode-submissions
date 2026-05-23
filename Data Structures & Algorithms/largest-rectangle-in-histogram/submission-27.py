class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        sol = 0

        for i, height in enumerate(heights):
            index = i
            while stack and height < stack[-1][1]:
                index, pHeight = stack.pop()

                sol = max(sol, (i-index)*pHeight)


            stack.append((index, height))

        for i, height in stack:
            sol = max(sol, (len(heights)-i)*height)

        return sol