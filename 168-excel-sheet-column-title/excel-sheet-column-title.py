class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = columnNumber 
        res=[]
        while col>0:
            col-=1
            res.append(chr(col%26 +ord('A')))
            col //=26
        return ''.join(res[::-1])