class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp_arr = [[0] * (len(weight) + 1) for i in range(capacity + 1)]
        # 4 by 6
        for r in range(capacity - 1, -1, -1):
            for c in range(len(weight) -1, -1, -1):
                if weight[c] + r > capacity:
                    dp_arr[r][c] = dp_arr[r][c+1]
                    continue
                
                dp_arr[r][c] = max(
                    dp_arr[r + weight[c]][c] + profit[c],
                    dp_arr[r + weight[c]][c+1] + profit[c],
                    dp_arr[r][c+1]
                )
        
        return dp_arr[0][0]

        # c = 4
        # profit = [1, 2, 4]
        # capacity=[2, 2, 4]
