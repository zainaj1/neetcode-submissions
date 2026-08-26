class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        i = 0
        return self.maxMem(i, cache, profit, weight, capacity)
    
    def maxMem(self, i, cache, profit: List[int], weight: List[int], capacity: int) -> int:
        if i >= len(profit):
            return 0
        elif (i, capacity) in cache:
            return cache[(i, capacity)]
        elif weight[i] > capacity:
            cache[(i, capacity)] = self.maxMem(i+1, cache, profit, weight, capacity)
        else:
            cache[(i, capacity)] = max(
                self.maxMem(i+1, cache, profit, weight, capacity - weight[i]) + profit[i],
                self.maxMem(i+1, cache, profit, weight, capacity)
            )

        return cache[(i, capacity)]

