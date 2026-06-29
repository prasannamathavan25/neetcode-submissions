class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int , int > book ; 

        int n = nums.size();


        for(int i = 0 ; i < n ; ++i)
        {
            int rem = target - nums[i]; 
            if( book.find(rem) != book.end())
            {
               return {book[rem] , i} ; 
            }
            book.insert({nums[i] , i });
        }
        return {};
    }
};
