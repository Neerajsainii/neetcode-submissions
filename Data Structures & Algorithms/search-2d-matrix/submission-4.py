class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        l2 = 0
        r1 = len(matrix) - 1
        r2 = len(matrix[0]) - 1
        for i in range(len(matrix)):
            mid1 = l1 + (r1-l1)//2
            print('mid1',mid1)
            if target > matrix[mid1][0]:
                l1 = mid1 + 1
            elif target < matrix[mid1][0]:
                r1 = mid1 - 1
            else:
                return True
        
        for i in range((len(matrix[0]))):
            mid2 = l2 + (r2-l2)//2
            print('mid2',mid2)
            if target > matrix[mid1][mid2]:
                l2 = mid2 + 1
            elif target < matrix[mid1][mid2]:
                r2 = mid2 - 1
            else:
                return True
        return False
        

        