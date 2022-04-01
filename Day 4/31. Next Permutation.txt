class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx1,idx2=0,0
        s=sorted(nums,reverse=True)
        if s==nums:
            nums.sort()
        else:
            for i in range(len(nums)-2,-1,-1):
                if nums[i]<nums[i+1]:
                    idx1=i
                    break
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[idx1]:
                    idx2=i
                    break
            nums[idx1],nums[idx2]=nums[idx2],nums[idx1]
            nums[idx1+1:]=nums[:idx1:-1]