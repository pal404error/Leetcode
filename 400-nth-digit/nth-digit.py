class Solution:
    def findNthDigit(self, n: int) -> int:
        d = b =1
        while n > 9*b*d:
            n-= 9*b*d
            d+=1
            b*=10
        q,r=divmod(n-1, d)
        return int(str(b+q)[r])