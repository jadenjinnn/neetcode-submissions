class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[0], height[r]

        sol = 0

        while l<r:
            if height[l]<height[r]:
                l += 1

                water = maxL - height[l]

                if water>0:
                    sol += water

                maxL = max(maxL, height[l])
            else:
                r -= 1
                water = maxR -height[r]

                if water>0:
                    sol += water
                    
                maxR = max(maxR, height[r])

            print(sol, l, r)

        return sol