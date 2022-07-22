class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        st=set()
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while(l<r):
                    s=nums[i]+nums[j]+nums[l]+nums[r]
                    if s<target:
                        l+=1
                    elif s>target:
                        r-=1
                    else:
                        if (nums[i],nums[j],nums[l],nums[r]) not in st:
                            st.add((nums[i],nums[j],nums[l],nums[r]))
                            ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
        return ans