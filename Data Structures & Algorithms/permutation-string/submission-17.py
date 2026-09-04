class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        book1 = [0]*26
        book2 = [0]*26

        for i in range(len(s1)):
            ind = ord(s1[i]) - ord('a')
            book1[ind] += 1

        for i in range(len(s1)):
            ind = ord(s2[i]) - ord('a')
            book2[ind] += 1  
        
        lp , rp = 0 , len(s1) - 1

        while rp < len(s2)-1:
            if book1 == book2 : 
                return True 
            ind = ord(s2[lp]) - ord('a')
            book2[ind] -= 1
            lp = lp + 1
            rp = rp + 1
            ind = ord(s2[rp]) - ord('a')
            book2[ind] += 1
        return book1 == book2
        
        

        


        

            
        
        