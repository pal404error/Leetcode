class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        string ans="";
        for(auto i:words){
            int c=i.length()-1;
            bool na=false;
            if(i.length() <= 1){
                ans = i;
                break;
            }
            for(int j=0;j<i.length()/2;j++){
                if(i[j] == i[c]){
                    c--;
                    na = true;
                }else{
                    na = false;
                    break;

                }
            }
            if(na == true){
                ans = i;
                break;
            }

        }
        return ans;
    }
};