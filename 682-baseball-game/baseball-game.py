class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r=[]
        for i in range(len(operations)):
            try:
                r.append(int(operations[i]))
            except ValueError:
                if operations[i]=="+":
                    r.append(r[-2]+r[-1])
                elif operations[i] == "D":
                    r.append(r[-1] * 2)
                elif operations[i] == "C":
                    r.pop()
        return sum(r)