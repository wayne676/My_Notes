class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    def climbStairsT(self, n: int) -> int:
        p,q,r=0,0,1
        for i in rane(n+1):
            p=q
            q=r
            r=p+q
        return r