class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                check=0
                try:
                    if j>0 and i>0 and (board[i-1][j-1]==1 or board[i-1][j-1]==3):
                        check+=1
                except:
                    pass
                try:
                    if i>0 and board[i-1][j]==1 or board[i-1][j]==3:
                        check+=1
                except:
                    pass
                try:
                    if i>0 and board[i-1][j+1]==1 or board[i-1][j+1]==3:
                        check+=1
                except:
                    pass
                try:
                    if j>0 and (board[i][j-1]==1 or board[i][j-1]==3):
                        check+=1
                except:
                    pass
                try:
                    if board[i][j+1]==1 or board[i][j+1]==3:
                        check+=1
                except:
                    pass
                try:
                    if j>0 and (board[i+1][j-1]==1 or board[i+1][j-1]==3):
                        check+=1
                except:
                    pass
                try:
                    if board[i+1][j]==1 or board[i+1][j]==3:
                        check+=1
                except:
                    pass
                try:
                    if board[i+1][j+1]==1 or board[i+1][j+1]==3:
                        check+=1
                except:
                    pass
                if board[i][j]==0:
                    if check==3:
                        board[i][j]=2
                    else:
                        board[i][j]=0
                elif board[i][j]==1:
                    if check==2 or check==3:
                        board[i][j]=1
                    else:
                        board[i][j]=3
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==3:
                    board[i][j]=0