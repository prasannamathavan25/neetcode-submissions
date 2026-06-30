class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book = dict()

        for loop1 in range(len(strs)):
            arr =[0]*26
            for loop2 in range(len(strs[loop1])):
                ch = strs[loop1][loop2]
                ind = ord(ch) - ord('a')
                arr[ind] += 1 
            key = tuple(arr)

            if key not in book : 
                book[key] = []
            
            book[key].append(strs[loop1])
        
        return list(book.values())


        