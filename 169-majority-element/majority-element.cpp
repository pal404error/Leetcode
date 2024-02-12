class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ma=0;
        unordered_map<int,int> map;
        for(auto i :nums){
            map[i]++;
        }
        
        for(auto i:map){
            ma = max(ma,i.second);
        }
        int ans=0;
        for(auto i:map){
            if(i.second == ma){
                ans = i.first;
            }
        }
        return ans;
    }

};