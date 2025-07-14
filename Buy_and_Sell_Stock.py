class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        maxprofit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            else:
                maxprofit = max(maxprofit, i - min_price)
        return maxprofit
