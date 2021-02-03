class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy,res=float('inf'),0
        for p in prices:
            minBuy=min(p,minBuy)
            res=max(res,p-minBuy)
        return res