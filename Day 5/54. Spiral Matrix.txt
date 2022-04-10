class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while len(matrix):
            try:
                ans+=matrix.pop(0)
                ans+=[i.pop() for i in matrix]
                ans+=matrix.pop()[::-1]
                ans+=[i.pop(0) for i in matrix][::-1]
            except:
                break
        return ans