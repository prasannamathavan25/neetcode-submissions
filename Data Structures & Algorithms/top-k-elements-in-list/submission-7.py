class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        book = dict()
        for loop in range(len(nums)):
            book[nums[loop]] = book.get(nums[loop] , 0) + 1 
        
        sorted_pairs = sorted(book.items() , key = lambda item : item[1] , reverse = True)
        print(sorted_pairs)
        return [pair[0]  for pair in sorted_pairs[:k]]
