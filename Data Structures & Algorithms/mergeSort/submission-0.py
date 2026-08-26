# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        if n <= 1:
            return pairs

        m = (n + 1) // 2
        left_side, right_side = self.mergeSort(pairs[0:m]), self.mergeSort(pairs[m:])
        return self.merge(left_side, right_side)
    
    # Assumes left and right are both sorted i.e left[i] < left[i+1] and right[j] < right[j+1]
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        
        new_list = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                new_list.append(left[i])
                i+=1
            else:
                new_list.append(right[j])
                j+=1 
        
        if i < len(left):
            new_list.extend(left[i:])
        elif j < len(right):
            new_list.extend(right[j:])
        
        return new_list

