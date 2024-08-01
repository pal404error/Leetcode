class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for m in details:
            age = m[11]
            age = age + m[12]
            if int(age) > 60:
                c = c+1
        
        return c
        