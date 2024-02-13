class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> map;
        for(auto i :nums){
            map[i]++;
        }
        int ans;
        for(auto n :map){
            if(n.second == 1){
                ans = n.first;
                return n.first;
                break;
            }
        }
        return ans;
    }
};