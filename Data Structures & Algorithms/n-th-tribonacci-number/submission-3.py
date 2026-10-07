class Solution:
    def tribonacci(self, n: int) -> int:
        # Base Cases
        if n == 0: 
            return 0
        if n == 1 or n == 2: 
            return 1
            
        # Initialize the first three values
        t0, t1, t2 = 0, 1, 1
        
        # Build forward up to n
        for _ in range(3, n + 1):
            next_val = t0 + t1 + t2
            
            # Shift variables forward
            t0 = t1
            t1 = t2
            t2 = next_val
            
        return t2
