'''You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.'''

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        bestfish = 0
        locfish = 0
        rbound = len(grid)
        cbound = len(grid[0])

        def getfish(r,c):
            fished = 0
            if (r>= 0 and r < len(grid)) and (c>=0 and c < len(grid[0])):
                if  grid[r][c] > 0:
                    fished =  grid[r][c]
                    grid[r][c] = 0
                    fished += getfish(r+1,c)
                    fished += getfish(r-1,c)
                    fished += getfish(r,c+1)
                    fished += getfish(r,c-1)
            return fished

        for r in range(0,rbound):
            for c in range(0,cbound):
                locfish = getfish(r,c)
                bestfish = max(bestfish,locfish)
        return bestfish



        

