class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global ans,d,s
        ans,s=0,0
        d=dict()
        d[0]=1
        def solver(r):
            global ans,d,s
            if not r:
                return 0
            #print(s)
            s+=r.val
            #print(s,"Af")
            if (s-targetSum) in d:
                ans+=d[s-targetSum]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
            solver(r.left)
            solver(r.right)
            if s in d:
                d[s]-=1
            s-=r.val
        solver(root)
        return ans