class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        cur_max = 0

        for i, height in enumerate(heights):
            start = i

            while stack and height < stack[-1][1]:
                index,h = stack.pop()
                cur_max = max(cur_max, (i-index)*h)
                start=index

            stack.append((start, height))

        for i, height in stack:
            cur_max = max(cur_max, (len(heights)-i)*height)

        return cur_max