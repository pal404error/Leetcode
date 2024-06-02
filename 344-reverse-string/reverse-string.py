class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = (len(s)//2)
        n1 = len(s)-1
        # print(n)
        for i in range(0,n):
            t = s[n1-i]
            print(t)
            s[n1-i] = s[i]
            s[i] = t

        

        