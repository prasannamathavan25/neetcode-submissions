class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> book;

        for (int loop1 = 0; loop1 < strs.size(); loop1++)
        {
            vector<int> arr(26, 0);

            for (int loop2 = 0; loop2 < strs[loop1].size(); loop2++)
            {
                char ch = strs[loop1][loop2];
                int ind = ch - 'a';
                arr[ind]++;
            }

            string key = "";

            for (int i = 0; i < 26; i++)
            {
                key += "#";
                key += to_string(arr[i]);
            }

            if (book.find(key) == book.end())
            {
                book[key] = {};
            }

            book[key].push_back(strs[loop1]);
        }

        vector<vector<string>> ans;

        for (auto &it : book)
        {
            ans.push_back(it.second);
        }

        return ans;
    }
};