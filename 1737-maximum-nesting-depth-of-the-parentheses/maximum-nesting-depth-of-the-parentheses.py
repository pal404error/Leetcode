class Solution:
    def maxDepth(self, s: str) -> int:
        stack =[]
        m =0
        if("(" not in s): return 0
        for a in s:
            if(a == "("):
                stack.append(1)
                m = max(m, len(stack))
            if( a == ")"):
                stack.pop()
            
        
        if(len(stack) == 0 and m ==0): return 1
        return m