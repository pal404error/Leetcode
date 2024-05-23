class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if i == "{" or i == "(" or i == "[":
                a.append(i)
            elif len(a) != 0 and a[-1] == "{" and i == "}":
                a.pop()
            elif len(a) != 0 and a[-1] == "(" and i == ")":
                a.pop()
            elif len(a) != 0 and a[-1] == "[" and i == "]":
                a.pop()
            
                
            else:
                return False
        
        return len(a) == 0