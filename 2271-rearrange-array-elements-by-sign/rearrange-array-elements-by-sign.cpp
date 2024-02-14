class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> t;
        int n=nums.size();
        queue<int> pos;
         queue<int> neg;
        for(auto i: nums){
            if(i>0){
                pos.push(i);
            }else{
                neg.push(i);
            }
            
        }
        for(int i=0;i<n/2;i++){
            t.push_back(pos.front());
            t.push_back(neg.front());
            pos.pop();
            neg.pop();
        }
        return t;

    }
};