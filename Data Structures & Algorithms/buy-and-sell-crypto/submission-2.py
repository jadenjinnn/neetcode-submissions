class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for i in range(1, len(prices)):
            j = 0

            while j+i < len(prices):
                print(i, j)
                best = max(best, prices[j+i]-prices[j])

                j += 1

        return best