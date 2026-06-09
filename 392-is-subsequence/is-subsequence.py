class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=0
        for i in s:
            j=s1
            while j<len(t):
                if t[j]==i:
                    s1=j+1
                    break
                j+=1
            if j==len(t):
                return False
        return True