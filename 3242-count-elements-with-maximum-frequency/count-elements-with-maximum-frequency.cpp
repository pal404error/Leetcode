class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int maxi=0,ele=0;
        unordered_map<int,int> map;
        for(auto i: nums) map[i]++;

        for(auto i: map){
            maxi = std::max(maxi,i.second);
            
        }
        for(auto i:map) if(maxi == i.second) ele+=maxi;

        return ele;
    }
};