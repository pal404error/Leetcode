class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> um;
        for(auto i: s){
            um[i]++;
        }
        int c=0;
        int od =0;
        for(auto i: um){
            if (i.second%2 == 1){
                od++;
            }
        }
        if (od > 1){
            return s.length() - od +1;
        }
        return s.length();
    }
};