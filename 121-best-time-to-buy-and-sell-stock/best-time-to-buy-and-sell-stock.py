class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        minprice = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - minprice 
            maxprofit = max(maxprofit,profit)
            minprice=min(minprice,prices[i])
        return maxprofit