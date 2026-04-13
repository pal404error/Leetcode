class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew=0
        for i in jewels:
            if i in stones:
                jew+=stones.count(i)
        return jew