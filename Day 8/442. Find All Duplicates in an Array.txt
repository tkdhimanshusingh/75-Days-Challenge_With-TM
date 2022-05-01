class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                ans.append(idx+1)
            nums[idx]=-nums[idx]
        return ans