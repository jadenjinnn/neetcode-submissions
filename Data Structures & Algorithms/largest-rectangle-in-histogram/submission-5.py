class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0

        for i, height in enumerate(heights):
            if not stack:
                stack.append((i, height))

            elif height >= stack[-1][1]:
                stack.append((i, height))
            else:
                popped = None
                while stack and height < stack[-1][1]:
                    popped = stack.pop()

                    max_height = max(popped[1] * (i-popped[0]), max_height)
                    # print(stack)

                stack.append((popped[0], height))
            
            # print(stack, max_height)

        while stack:

            popped = stack.pop()

            max_height = max(max_height, (len(heights) - popped[0]) * popped[1])

            # print(stack, max_height)


        return max_height
        