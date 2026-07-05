class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        book = {}

        for num in nums:
            book[num] = book.get(num, 0) + 1


        # Step 2: Frequency buckets
        table = [[] for _ in range(len(nums) + 1)]

        for key, value in book.items():
            table[value].append(key)


        # Step 3: Traverse from highest frequency
        ans = []

        ptr = len(nums)

        while ptr > 0:

            for num in table[ptr]:
                ans.append(num)

                if len(ans) == k:
                    return ans

            ptr -= 1