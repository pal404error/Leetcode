class Solution:
    def isValid(self, s: str) -> bool:
        temp = s
        while temp:
            if not "abc" in temp:
                return False
            temp = temp.replace("abc", '')
        return True

                