class Solution:
    def maxDepth(self, s: str) -> int:
        c =0
        m =0
        if("(" not in s): return 0
        for a in s:
            if(a == "("):
                c+=1
                m = max(m, c)
            if( a == ")"):
                c-=1
            
        return m