# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        start = 0
        end = len(pairs) - 1
        pivot = end
        self.quickSortHelper(start, end, pivot, pairs)
        return pairs
    """
    pairs = [(3, "cat"), (2, "dog"), (3, "bird")]


    quickSortHelper(0, 2, 2, [(3, "cat"), (2, "dog"), (3, "bird")])  
    start = 3 
    end = 2
    pivot = 2
    insert = 2
    

    """
    def quickSortHelper(self, start: int, end: int, pivot: int, paris: List[Pair]) -> None:
        initital = start
        if start >= end:
            return None

        insert = start
        while start <= end:
            if insert == pivot:
                insert += 1
            if pairs[start].key < pairs[pivot].key :
                temp = pairs[insert] 
                pairs[insert] = paris[start]
                pairs[start] = temp
                insert += 1
            start += 1

            if start == pivot:
                start += 1


        if insert != pivot:
                temp = pairs[insert] 
                pairs[insert] = paris[pivot]
                pairs[pivot] = temp 
        
        self.quickSortHelper(initital, insert-1, insert-1, pairs)
        self.quickSortHelper(insert+1, end, end, pairs)





            


        