class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]

        vol = 0

        while l<r:
            if maxL < maxR:
                l += 1
                sol = maxL - height[l]

                if sol>0:
                    vol += sol

                maxL = max(maxL, height[l])
            else:
                r -= 1
                sol = maxR - height[r]

                if sol>0:
                    vol += sol

                maxR = max(maxR, height[r])

        return vol