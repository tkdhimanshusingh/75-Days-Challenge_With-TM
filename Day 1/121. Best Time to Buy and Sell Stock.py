class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        b=prices[0]
        for i in range(1,len(prices)):
            d=prices[i]-b
            b=min(b,prices[i])
            p=max(p,d)
        return p