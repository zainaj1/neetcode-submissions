class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (len(weight)+1) for i in range(capacity+1)]
        print(len(dp), len(dp[0]))
        for r in range(capacity, -1, -1):
            for c in range(len(weight)-1, -1, -1):
                if weight[c] + r > capacity:
                    dp[r][c] = dp[r][c+1]
                    continue
                dp[r][c] = max(dp[r+weight[c]][c+1] + profit[c], dp[r][c+1])
                
                
        return dp[0][0]