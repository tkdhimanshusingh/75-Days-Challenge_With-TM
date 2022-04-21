class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[]
        m=0
        rstk,lstk=[],[]
        r,l=[0]*len(heights),[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while rstk and rstk[-1][0]>=heights[i]:
                rstk.pop()
            if rstk:
                r[i]=rstk[-1][1]
            else:
                r[i]=len(heights)
            rstk.append([heights[i],i])
            
        for i in range(len(heights)):
            while lstk and lstk[-1][0]>=heights[i]:
                lstk.pop()
            if lstk:
                l[i]=lstk[-1][1]
            else:
                l[i]=-1
            lstk.append([heights[i],i])
        
        for i in range(len(heights)):
            m=max(m,(r[i]-l[i]-1)*heights[i])
        return m