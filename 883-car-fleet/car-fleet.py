class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = [[p,s] for p,s in zip(position, speed)]
        
        stac =[]
        for p,s in sorted(p)[::-1]:
            stac.append((target-p)/s)
            if len(stac)>=2 and stac[-1]<= stac[-2]:
                stac.pop()
        
        return len(stac)