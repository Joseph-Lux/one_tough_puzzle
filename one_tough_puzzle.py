####################################
# heart = 1
# spade = 2
# clubs = 3
# diamond = 4
# hole is negative of shape
####################################

pieces = [
    [3, 1, -4, -3],
    [-3, 2, 2, -1],
    [4, -4, -1, 1],
    [-3, -4, 4, 3],
    [-2, -1, 3, 1],
    [-3, 1, 4, -3],
    [-1, -4, 2, 4],
    [-2, -1, 2, 4],
    [2, -2, -3, 1]
]

solution = []

def removeR(array, num):
    newArray = array.copy()
    newArray.remove(num)
    return newArray

def rotate(array, i):
    return [array[(x + i) % 4] for x in range(4)]

def findNextPiece(num, pieces):
    global solution
    if num == 9:
        for i in solution:
            print(i)
        exit()
    for piece in pieces:
        for i in range(4):
            if piece[(checks[num][0][0] + i) % 4] == -solution[checks[num][0][1]][checks[num][0][2]]:
                if (len(checks[num]) == 2):
                    if piece[(checks[num][1][0] + i) % 4] == -solution[checks[num][1][1]][checks[num][1][2]]:
                        solution.append(rotate(piece, i))
                        findNextPiece(num + 1, removeR(pieces, piece))
                        solution.pop()
                else:
                    solution.append(rotate(piece, i))
                    findNextPiece(num + 1, removeR(pieces, piece))
                    solution.pop()
        

# (my side, other piece, other piece's side)
checks = [
    [], # 0 
    [(2, 0, 0)], # 1
    [(3, 1, 1)], # 2
    [(0, 2, 2), (3, 0, 1)], # 3
    [(0, 3, 2)], # 4
    [(1, 4, 3), (0, 0, 2)], # 5
    [(1, 5, 3)], # 6
    [(2, 6, 0), (1, 0, 3)], # 7
    [(2, 7, 0), (1, 1, 3)] # 8
]

for middlePiece in pieces:
    solution.append(middlePiece)
    findNextPiece(1, removeR(pieces, middlePiece))
    solution.pop()