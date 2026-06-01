class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy, sell = 0, 0

        while sell < len(prices):
            if prices[sell]<prices[buy]:
                buy = sell
            else:
                best = max(best, prices[sell]-prices[buy])

            sell += 1

        return best