class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        curr=prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-curr
            maxprofit = max(maxprofit,profit)
            curr = min(curr,prices[i])
        return maxprofit
        