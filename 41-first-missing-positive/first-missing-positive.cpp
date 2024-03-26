class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int m=0;
        if(nums.size() == 1 && nums[0] == 1){

        }
        for(auto i:nums) m = max(m,i);
        sort(nums.begin(), nums.end());
        for(int i=1;i<m;i++){
            if(binary_search(nums.begin(), nums.end(), i)){

            }else return i;
        
        }
        return m+1;
    }
};