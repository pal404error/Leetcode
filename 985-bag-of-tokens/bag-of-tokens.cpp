class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int score=0, maxs=0, l=0, r=tokens.size()-1;
        while(l<=r){
            if(power >= tokens[l]){
                power-= tokens[l];
                score++;
                l++;
                maxs = max(maxs, score);
            }else if( score>0){
                power += tokens[r];
                score -- ;
                r -- ;
            }
            else{
                break;
            }
        }
        return maxs;
    }
};