class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s,l = 0, int(math.sqrt(c))
        # print(l)
        while s<=l:
            sum = (s*s) + (l*l)
            if sum == c:
                return True
            elif sum < c:
                s+=1
            elif sum>c:
                l-=1
        
        
        return False