class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book = dict()

        for item in strs:
            arr = [0]*26
            for ch in item:
                ind = ord(ch) - ord('a')
                arr[ind] = arr[ind] + 1
            key = tuple(arr)
            if key not in book:
                book[key] = []
            book[key].append(item)
        
        return list(book.values())
        

        