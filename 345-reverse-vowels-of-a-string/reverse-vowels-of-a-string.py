class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = [i for i in s if i in "aeiouAEIOU"]
        res = [ i if i not in "aeiouAEIOU" else vow.pop() for i in s]
        return "".join(res)