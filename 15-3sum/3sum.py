class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 3:
        #     t = nums[0] + nums[1] + nums[2]
        #     if t == 0:
        #         return nums

        nums.sort()
        n= len(nums)
        print(nums)
        ans = []
        for i in range(n):
            target = -nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while(j<k):
                s = nums[k] +nums[j] +nums[i]
                if (s) ==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+= 1 
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        
        return ans