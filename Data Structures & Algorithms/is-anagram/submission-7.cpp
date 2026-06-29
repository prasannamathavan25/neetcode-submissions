class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map< char , int> book1 ; 
        unordered_map<char , int> book2 ; 

        if (s.size() != t.size()){
            return false ;
        }

        for( int i = 0 ; i < s.size() ; ++ i){
            book1[s[i]]++ ; 
            book2[t[i]]++ ; 
        }

        return book1 == book2 ; 

        
    }
};
