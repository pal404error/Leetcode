class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = "qwertyuiopQWERTYUIOP"
        s2 = "asdfghjklASDFGHJKL"
        s3 = "zxcvbnmZXCVBNM"

        key = ''
        same = True
        res = []

        for i in words:
            same = True
            if i[0] in s1:
                key = s1
            elif i[0] in s2:
                key = s2
            else:
                key = s3

            for j in range(1, len(i)):
                if i[j] not in key:
                    same = False
            if same:
                res.append(i)

        return res