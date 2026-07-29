from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. Create a list of lists: [[distance, number], [distance, number], ...]
        mybook = []
        for num in arr:
            dis = abs(x - num)
            item = [dis, num] 
            mybook.append(item)
        
        # 2. Sort using our general rule:
        # Primary: distance (item[0]) ascending
        # Secondary: number (item[1]) ascending (tie-breaker)
        sorted_book = sorted(mybook, key=lambda item: (item[0], item[1]))
        
        # 3. Take the first k elements and extract the original numbers
        ans = [item[1] for item in sorted_book[:k]]
        
        # 4. LeetCode requires the final answer list to be sorted from small to large
        return sorted(ans)
