class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0

        l, r = 0, len(heights)-1

        while l<r:
            sol = max(sol, min(heights[l], heights[r])*(r-l))

            print(l, r, sol, min(heights[l], heights[r])*(r-l))

            if heights[l]>heights[r]:
                r -= 1
            else:
                l += 1

        return sol