class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> book;

        for (int i = 0; i < nums.size(); ++i)
        {
            int rem = target - nums[i];

            if (book.find(rem) != book.end())
            {
                return {book[rem], i};
            }

            book.emplace(nums[i], i);
            // or: book[nums[i]] = i;
        }

        return {};
    }
};