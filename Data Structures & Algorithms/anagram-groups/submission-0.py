class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        book = defaultdict(list)

        for s in strs: 
            table = [0]*26

            for c in s : 
                num = ord(c) - ord('a')
                table[num] = table[num] + 1 
            
            table = tuple(table)
            book[table].append(s)
        
        return list(book.values())
        