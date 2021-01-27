# https://leetcode.com/problems/decode-ways/
class Solution(object):
    def numDecodings(self,s):
        if s[0]=='0' or not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[0:2]=[1,1]
        for i in range(2,len(s)+1):
            if 0<int(s[i-1])<10:
                dp[i]+=dp[i-1]
            if 10<=int(s[i-2:i])<27:
                dp[i]+=dp[i-2]
        return dp[-1]