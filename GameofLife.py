'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
  
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        import copy
        nextboard = copy.deepcopy(board)

        for r in range(0,m):
            for c in range(0,n):
                csum = 0
                neighbors = 0
                #print("cell " + str(r) + "," + str(c))
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if (i > -1 and j > -1) and (i < m and j < n):
                            #print("add " + str(i) + "," + str(j))
                            csum += int(board[i][j])
                csum = csum - int(board[r][c])
                #print('csum =' + str(csum))
                if csum < 2 and board[r][c] == 1:
                    nextboard[r][c] = 0
                    #print('dies')
                elif (csum == 2 or csum == 3) and board[r][c] == 1:
                    nextboard[r][c] = 1
                    #print('lives')
                elif csum > 3 and board[r][c] == 1:
                    nextboard[r][c] = 0
                    #print('dies')
                elif csum == 3 and board[r][c] == 0:
                    nextboard[r][c] = 1
                    #print('revives')
                #else:
                    #print('dead')

        for r in range(0,m):
            for c in range(0,n):
                board[r][c] = int(nextboard[r][c])
        
