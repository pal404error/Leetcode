class Solution {
public:
    bool halvesAreAlike(string s) {
        string first = s.substr(0,s.length()/2);
        string second = s.substr(s.length()/2);
        int f=0,w=0;
        vector<char> a {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        for(int i=0;i<first.length(); i++){
            if (find(a.begin(), a.end(), first[i]) != a.end()) f++;
            if (find(a.begin(), a.end(), second[i]) != a.end()) w++;
        }
        return f == w;
    }
};