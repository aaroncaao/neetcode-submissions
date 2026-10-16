class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            tempP = sell - minBuy
            if sell < minBuy:
                minBuy = sell
            if maxP < tempP:
                maxP = tempP
        
        return maxP