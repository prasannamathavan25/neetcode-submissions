class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        int lp = 0 ;
        int rp = nums.size() -1 ;

        while( lp<=rp ){

            if(nums[lp] != val){
                lp = lp + 1 ; 
                continue ;
            }
            if(nums[rp] ==val){
                rp = rp -1 ;
                continue ;
            }
            nums[lp] = nums[rp] ;
            lp = lp + 1 ;
            rp = rp -1 ;
        }

        return lp ;


        
    }
};