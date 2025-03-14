class Solution:
    def count(self, coins, tsum):
        # code here 
        dp = [0] * (tsum + 1)
        dp[0] = 1 
        for coin in coins:
            for j in range(coin,tsum+1):
                dp[j]+=dp[j-coin]
        return dp[tsum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends