class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> hash;

        for (string s : strs)
        {
            vector<int> freq(26, 0);

            // Count frequency of each character
            for (char ch : s)
            {
                freq[ch - 'a']++;
            }

            // Build a unique key
            string key = "";

            for (int x : freq)
            {
                key += "#";
                key += to_string(x);
            }

            // Add the string to its group
            hash[key].push_back(s);
        }

        // Collect all groups
        vector<vector<string>> ans;

        for (auto &[key, group] : hash)
        {
            ans.push_back(group);
        }

        return ans;
    }
};