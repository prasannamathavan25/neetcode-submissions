class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix) , len(matrix[0])
        for r in range(m):
            if matrix[r][0] == target:
                return True 
            if matrix[r][0] < target : 
                continue
            r = r -1 
            break
        

        row = r 
        arr = matrix[row]
        print(arr)
        lp = 0 
        rp = n-1

        while lp <= rp : 
            mid = (lp + rp)//2
            if target == arr[mid]:
                return True 
            elif arr[mid] >target:
                rp = mid -1  
            else:
                lp = mid +1 
        
        return False
        
        
        