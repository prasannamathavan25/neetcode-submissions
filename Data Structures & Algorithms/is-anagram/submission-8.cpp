class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        // Uses exactly 26 * 4 bytes = 104 bytes of memory!
        int counts[26] = {0}; 

        for (int i = 0; i < s.size(); ++i) {
            counts[s[i] - 'a']++; // Maps 'a' to 0, 'b' to 1, etc.
            counts[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; ++i) {
            if (counts[i] != 0) return false;
        }

        return true;
    }
};
