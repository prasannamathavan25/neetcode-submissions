class Solution {
public:
    bool hasDuplicate(vector<int>& nums)
    {
        unordered_set<int> book ; 
        for(int ind = 0 ; ind< nums.size() ; ++ind)
        {
            if( book.count(nums[ind]))
            {
                return true;
            }
            book.insert(nums[ind]);
        }
        return false;
        
    }
};