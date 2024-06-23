
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        
        qinc = deque([])
        qdec = deque([])
        l = 0
        
        mlen = 1
        for i in range(len(nums)):
            while qinc and nums[qinc[-1]] > nums[i]:
                qinc.pop()
            qinc.append(i)
            
            while qdec and nums[qdec[-1]] < nums[i]:
                qdec.pop()
            qdec.append(i)
            
            while nums[qdec[0]] - nums[qinc[0]] > limit:
                l += 1
                if qdec[0] < l:
                    qdec.popleft()
                if qinc[0] < l:
                    qinc.popleft()
            
            mlen = max(mlen, i-l+1)
            
        return mlen