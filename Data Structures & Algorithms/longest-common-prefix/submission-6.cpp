class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        string ans = "";
        int n = strs[0].size();

        for (int loop = 0; loop < n; ++loop)
        {
            char cur = strs[0][loop];

            for (int i = 1; i < strs.size(); ++i)
            {
                if (loop >= strs[i].size() || strs[i][loop] != cur)
                {
                    return ans;
                }
            }

            ans += cur;
        }

        return ans;
    }
};