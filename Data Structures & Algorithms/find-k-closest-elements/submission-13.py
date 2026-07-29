from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Step 1: Use Binary Search to find where 'x' would fit in 'arr'
        # 'idx' is the index of the first element greater than or equal to 'x'
        idx = bisect.bisect_left(arr, x)
        
        # Step 2: Initialize our window boundaries around 'idx'
        # 'l' and 'r' point to the elements we are currently comparing
        l = idx - 1
        r = idx
        
        # Step 3: Expand the window until it contains exactly 'k' elements
        # (r - l - 1) calculates the total number of elements inside our window
        while (r - l - 1) < k:
            # Handle out-of-bounds cases first
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            # Core logic: Compare distances to x
            # Left element is closer OR distances tie (choose smaller number 'l')
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
                
        # Step 4: Return the elements within the window using slicing
        # 'l + 1' excludes the left outer boundary pointer
        # 'r' excludes the right outer boundary pointer (slicing is exclusive at the end)
        return arr[l + 1 : r]
