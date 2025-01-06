'''
959. Regions Cut By Slashes
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
'''
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        #create regions
        n = len(grid)*3
        grid2 = [['1'] * n for i in range(n)]
        r_off = 0
        c_off = 0
        for row in grid:
            chars = list(row)
            print(chars)
            for c in chars:
                if c == '\\':
                    grid2[0+r_off][0+c_off] = '0'
                    grid2[1+r_off][1+c_off] = '0'
                    grid2[2+r_off][2+c_off] = '0'
                if c == '/':
                    grid2[0+r_off][2+c_off] = '0'
                    grid2[1+r_off][1+c_off] = '0'
                    grid2[2+r_off][0+c_off] = '0'
                c_off += 3
            r_off += 3
            c_off = 0

        #flood islands
        def islandflood(r,c):
            #valid location
            if (r>= 0 and r < len(grid2)) and (c>=0 and c < len(grid2[0])):
                #in island
                if grid2[r][c] == '1':
                    grid2[r][c] = '0'
                    islandflood(r+1,c)
                    islandflood(r-1,c)
                    islandflood(r,c+1)
                    islandflood(r,c-1)

        numisland = 0
        for r in range(0,len(grid2)):
            for c in range(0,len(grid2[0])):
                if grid2[r][c] == '1':
                    numisland += 1
                    islandflood(r,c)

        return numisland 
