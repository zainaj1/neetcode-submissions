# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

"""
case 4, 3, 2, 1
i = 1
j = 0

"""
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        
        for i in range(len(pairs)):
            j = i-1
           
            while j >= 0 and pairs[j+1].key < pairs[j].key: # first iteration j+1 = i bc j = i-1
                # Since we check if [j+1] < [j], we can assume that conditon holds true in this loop      
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp
                j -= 1
                
            states.append(pairs[:])

        return states

        
        