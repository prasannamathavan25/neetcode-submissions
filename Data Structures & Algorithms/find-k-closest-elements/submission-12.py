from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. Create a list of lists: [[distance, number], [distance, number], ...]
        mybook = []
        for i , num in enumerate(arr):
            dis = abs(x - num)
            item = [dis , num]
            mybook.append(item)
        
        sorted_arr = sorted(mybook , key = lambda  item: (item[0] , item[1]))
        ans = sorted([item[1] for item in sorted_arr[:k]])
        return ans