class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> m1;
        for(auto i:nums1) m1[i]++;

        unordered_map<int,int> m2;
        for(auto i:nums2) m2[i]++;

        unordered_map<int,int> com;
        for(auto i:m1) com[i.first]++;
        for(auto i:m2) com[i.first]++;

        vector<int> ans;
        for(auto i: com){
            if(i.second >= 2){
                ans.push_back(i.first);
            }
        }
        return ans;
    }
};