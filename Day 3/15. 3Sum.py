class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0 or len(nums)==1:
            return []
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if t==0:
                    if [nums[i],nums[l],nums[r]] not in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif t<0:
                    l+=1
                elif t>0:
                    r-=1
        return ans