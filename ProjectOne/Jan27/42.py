#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        lMax,rMax=float('-inf'),float('-inf')
        res=0
        while l<r:
            lMax=max(height[l],lMax)
            rMax=max(height[r],rMax)
            if lMax<rMax:
                res+=lMax-height[l]
                l+=1
            else:
                res+=rMax-height[r]
                r-=1
        return res

