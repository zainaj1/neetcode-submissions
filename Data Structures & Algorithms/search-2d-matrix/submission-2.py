class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l<=r:
            mid = (l+r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                print(matrix[mid])
                return self.binarySearch(matrix[mid], target)
        
        return False
    
    def binarySearch(self, row: List[int], target) -> bool:
        l = 0 
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2
            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1 
            else:
                return True
        
        return False

            
        