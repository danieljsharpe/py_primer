'''
Algorithm to solve the following checkerboard problem recursively:
How to cover a checkerboard that has one *corner* square missing, using L-shaped tiles comprising of 3 blocks that may be rotated but
may not overlap.
The strategy is to split the board into 4 quarters, and for 3 of these subboards a single tile is placed to cover the corner. The 3
subboards can be entirely covered (completely), leaving the fourth to be divided into quarters again. The base case is four-square
boards. At the end of the algorithm there are therefore 3 squares left to cover in a L-shape.
The side lengths of the board must be 2^k where k is an integer.
'''

from random import randint

def checkerboard(board,lab=1,top=0,left=0,side=None):
    if side is None: side = len(board)
    s = side // 2 # side length of subboard
    offsets = (0, -1), (side - 1, 0) # offsets for outer/inner squares of subboards

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top + dy_outer][left + dx_outer]:
                board[top + s + dy_inner][left + s + dx_inner] = lab
    # Next label
    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                # recursive calls, if s is at least 2
                lab = checkerboard(board, lab, top+dy, left+dx, s)
    # Return the next available label
    return lab


#Driver code
z = 8 # board length (must be = 2^k)
board = [[0]*z for i in range(z)] # initialise board
#set missing corner at random
cornerindex = (0, z-1)
r1 = randint(0,1)
r2 = randint(0,1)
board[cornerindex[r1]][cornerindex[r2]] = -1
lab = checkerboard(board)
for row in board:
    print ((" %2i"*z) % tuple(row))
