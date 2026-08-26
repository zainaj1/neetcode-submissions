class Solution:

    """
    list of piles of bananas 
    h is the number of hours you have to eat all the bananas
    k is how many bananas can be eatten in an hour 

    if pile is less than k we can eat all the bananas but it will still take us 1 hour i.e if our rate was 9 but each pile only had 2 bananas it would still take us an hour per pile
    We want to find the smallest k that satisfies our condition, this means minimum time is always len(piles)
    
    l = 18
    r = 30
    k = 17

    """ 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        solution = 0
        while l <= r:
            k = (l + r) // 2
            result = self.guessMin(piles, k, h)
            if result < 0: # Did not finsish bananas in time
                l = k + 1
            else:
                solution = k
                r = k - 1

        return solution

    def guessMin(self, piles, k, h):
        cost = 0
        for pile in piles:
            cost += math.ceil(pile / k)

        if cost > h:
            return -1
        else:
            return 1

        