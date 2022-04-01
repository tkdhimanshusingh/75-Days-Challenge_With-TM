class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        ans=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[l]**2<nums[r]**2:
                ans[i]=nums[r]**2
                r-=1
            else:
                ans[i]=nums[l]**2
                l+=1
        return ans