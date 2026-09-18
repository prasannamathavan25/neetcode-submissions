class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = {}

        # Count frequency
        for item in nums:
            if item not in book:
                book[item] = 0
            book[item] += 1

        # Sort by frequency
        sorted_book = sorted(
            book.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Take top k elements
        ans = []

        for i in range(k):
            ans.append(sorted_book[i][0])

        return ans