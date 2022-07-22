class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans,temp=[],[]
        def ksum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    temp.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])
                    temp.pop()
                return
            l,r=start,len(nums)-1
            while l<r:
                s=nums[l]+nums[r]
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    ans.append(temp+[nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        ksum(4,0,target)
        return ans