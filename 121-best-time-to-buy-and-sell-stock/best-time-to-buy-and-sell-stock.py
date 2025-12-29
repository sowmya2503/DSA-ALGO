class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            profit = prices[i]-curr 
            curr=min(curr,prices[i])
            maxprofit=max(maxprofit,profit)
        return maxprofit
        