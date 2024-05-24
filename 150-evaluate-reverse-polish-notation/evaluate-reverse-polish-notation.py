class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                a= int(s.pop())
                b = int(s.pop())
                w = a+b
                s.append(w)
            elif i == "-":
                a= int(s.pop())
                b = int(s.pop())
                w = b-a
                s.append(w)
            elif i == "/":
                a= int(s.pop())
                b = int(s.pop())
                w = b/a
                s.append(w)
            elif i == "*":
                a= int(s.pop())
                b = int(s.pop())
                w = a*b
                s.append(w)
            else:
                s.append(i)
            
        return int(s[-1])