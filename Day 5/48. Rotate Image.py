class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp=[[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        a,j=0,0
        for _ in range(len(matrix)):
            b=0
            for i in range(len(matrix)-1,-1,-1):
                temp[a][b]=matrix[i][j]
                b+=1
            j+=1
            a+=1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=temp[i][j]