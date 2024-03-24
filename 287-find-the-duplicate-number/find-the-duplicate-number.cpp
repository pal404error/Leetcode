class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=0,ans=0;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){

            n =nums[i] ^ nums[i+1] ;

            if(n == 0) {ans = nums[i];break;}
        } 
        
        return ans;
    }
};