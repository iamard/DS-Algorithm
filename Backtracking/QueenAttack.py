def isLegalPos(table, row, col):
    for i in range(col):
        if table[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if table[i][j]:
            return False
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if table[i][j]:
            return False
    return True

def findSolution(table, col):
    if (col >= 4):
        return True
    else:
        for row in range(4):
            if isLegalPos(table, row, col):
                table[row][col] = 1
                if findSolution(table, col + 1):
                    return True
                table[row][col] = 0
    return False

def printSolution(table):
    for i in range(4):
        print(table[i])
    
def queenAttack():
    table = [[0 for x in range(4)] for x in range(4)]

    if findSolution(table, 0):
        printSolution(table)

if __name__ == "__main__":
    queenAttack()
