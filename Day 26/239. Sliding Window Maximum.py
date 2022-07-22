from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,0
        q=deque()
        ans=[]
        while(j<len(nums)):
            #calculations
            while q and nums[j]>q[-1]:
                q.pop()
            q.append(nums[j])
            if (j-i+1)<k:
                j+=1
            elif (j-i+1)==k:
                #answer
                ans.append(q[0])
                #slide the window
                if nums[i]==q[0]:
                    q.popleft()
                i+=1
                j+=1
        return ans