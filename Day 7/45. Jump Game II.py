class Solution:
    def jump(self, nums: List[int]) -> int:
        lb=ub=0
        cnt=0
        while ub<len(nums)-1:
            max_jump=0
            for i in range(lb,ub+1):
                max_jump=max(max_jump,i+nums[i])
            lb=ub+1
            ub=max_jump
            cnt+=1
        return cnt