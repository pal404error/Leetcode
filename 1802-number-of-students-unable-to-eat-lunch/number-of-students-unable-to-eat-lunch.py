class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        sand = sandwiches
        c1 = students.count(1)
        c0 = students.count(0)
        for s in sand:
            if(s == 0 and c0 == 0):
                return c1
            if( s == 1 and c1 == 0):
                return c0
            if( s == 0 ):
                c0 -= 1
            else:
                c1-=1
            
        
        return 0