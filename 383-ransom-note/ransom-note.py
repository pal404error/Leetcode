class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(magazine) , Counter(ransomNote)
        if st1 & st2 == st2:
            return True
        return False