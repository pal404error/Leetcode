class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans =[]
        
        def back(op,cl,s):
            if len(s)== n*2:
                ans.append(s)
                return
            
            if op < n:
                back(op+1, cl, s+"(")
            if cl < op:
                back(op, cl+1, s+")")
            
        back(0,0,'')
        return ans