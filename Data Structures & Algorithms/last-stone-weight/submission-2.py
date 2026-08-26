import heapq

class Solution:
    """
    Creating the intial heap o(n)
    loop is at most n times (each smash reduces the list by 1)
    getting the first and second largest rocks are logn time 

    So we have logn + n * 2logn which gives us nlogn time
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) # o(n)
        while len(stones) > 1: # o(n)
            largest_stone = heapq.heappop_max(stones) # o(logn)
            second_largest_stone = heapq.heappop_max(stones) # o(logn)

            smash_result = abs(largest_stone - second_largest_stone) 

            if smash_result > 0:
                heapq.heappush_max(stones, smash_result)

        return heapq.heappop_max(stones) if len(stones) >= 1 else 0 


        