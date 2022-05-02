class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        cnt=0
        if k==0:
            for i in d.values():
                if i>1:
                    cnt+=1
            return cnt
        for j in d.keys():
            if k<0:
                return 0
            if j-k in d:
                cnt+=1
        return cnt