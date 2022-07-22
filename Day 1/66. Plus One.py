class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        s=int(s)
        s+=1
        s=str(s)
        ans=[]
        for i in s:
            ans.append(int(i))
        return ans