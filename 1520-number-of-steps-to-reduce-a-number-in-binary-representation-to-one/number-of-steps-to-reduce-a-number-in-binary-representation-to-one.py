class Solution:
    def numSteps(self, s: str) -> int:
        a = int(s, 2)
        n=0
        while True:
            # print(a)
            if a == 1:
                break
            if a%2 == 0:
                n+=1
                a = a// 2
            else:
                n+= 1
                a+=1
        
        return n
        