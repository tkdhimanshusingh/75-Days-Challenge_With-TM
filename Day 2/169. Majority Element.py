
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=nums[0]
        cnt=1
        for i in range(1,len(nums)):
            if cnt==0:
                element=nums[i]
            if element==nums[i]:
                cnt+=1
            else:
                cnt-=1
        return element