class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> c;
        for(int i=0;i<nums.size()-1;i++){
            int n = nums[i]^nums[i+1];
            if(n == 0){
                c.push_back(nums[i]);
            }
        }
        return c;
    }
};