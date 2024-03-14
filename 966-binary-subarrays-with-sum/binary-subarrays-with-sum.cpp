class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int,int> count;
        count[0]=1;
        int curr=0, total=0;
        for(auto i:nums){
            curr+=i;
            if(count.find(curr-goal) != count.end()){
                total+= count[curr-goal];
            }
            count[curr]++;

        }
        return total;
    }
};