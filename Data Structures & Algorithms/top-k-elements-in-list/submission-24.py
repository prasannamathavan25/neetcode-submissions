from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = Counter(nums)
        ans = [item[0] for item in book.most_common(k)]
        return ans
      
