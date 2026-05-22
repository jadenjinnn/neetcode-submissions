class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            mid = l + (r-l)//2

            speed = 0

            for pile in piles:
                speed += math.ceil(pile / mid)

            if speed <= h:
                res = mid
                r = mid-1
            else:
                l=mid+1

        return res
            